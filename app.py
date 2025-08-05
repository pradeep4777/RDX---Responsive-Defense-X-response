from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
import random
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()  # Load from .env

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

# -------------------- MySQL Connection --------------------
db = mysql.connector.connect(
    host="localhost",
    user="rdxuser",
    password="roshan",
    database="rdx_auth"
)
cursor = db.cursor()

# -------------------- Send OTP Email --------------------
def send_otp_email(to_email, otp):
    sender_email = os.getenv("SENDER_EMAIL")
    sender_password = os.getenv("SENDER_PASSWORD")

    msg = MIMEText(f"Your OTP for RDXSERVER is: {otp}")
    msg['Subject'] = 'RDXSERVER - OTP Verification'
    msg['From'] = sender_email
    msg['To'] = to_email

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, sender_password)
            smtp.send_message(msg)
        return True
    except Exception as e:
        print("Email Error:", e)
        return False

# -------------------- Home Page --------------------
@app.route('/')
def home():
    return render_template('index.html', username=session.get('username'))

# -------------------- About Page --------------------
@app.route('/about')
def about():
    if 'email' not in session:
        flash('Please log in to access this page.', 'warning')
        return redirect(url_for('login'))

    cursor.execute("SELECT * FROM rdxusers WHERE email = %s", (session['email'],))
    user_data = cursor.fetchone()

    if user_data:
        user = {
            'firstname': user_data[1],
            'lastname': user_data[2],
            'department': user_data[3],
            'mobile': user_data[4],
            'email': user_data[5]
        }
        return render_template('about.html', user=user)
    else:
        flash('User not found.', 'danger')
        return redirect(url_for('login'))

# -------------------- Register with OTP --------------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if 'otp' in request.form:
            if request.form['otp'] == session.get('otp'):
                data = session.get('temp_user_data')
                hashed_password = generate_password_hash(data['password'])

                cursor.execute("""
                    INSERT INTO rdxusers (firstname, lastname, department, mobile, email, password)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, (data['firstname'], data['lastname'], data['department'],
                      data['mobile'], data['email'], hashed_password))
                db.commit()

                session.pop('otp', None)
                session.pop('temp_user_data', None)

                flash('Registration successful! Please login.', 'success')
                return redirect(url_for('login'))
            else:
                flash('Invalid OTP. Please try again.', 'danger')
                return render_template('register.html', show_otp=True)

        # Step 1 - form data
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        department = request.form['department']
        mobile = request.form['mobile']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash('Passwords do not match.', 'danger')
            return render_template('register.html')

        cursor.execute("SELECT * FROM rdxusers WHERE email = %s", (email,))
        if cursor.fetchone():
            flash('Email already registered.', 'warning')
            return render_template('register.html')

        otp = str(random.randint(100000, 999999))
        session['otp'] = otp
        session['temp_user_data'] = {
            'firstname': firstname,
            'lastname': lastname,
            'department': department,
            'mobile': mobile,
            'email': email,
            'password': password
        }

        if send_otp_email(email, otp):
            flash('OTP sent to your email. Please verify.', 'info')
            return render_template('register.html', show_otp=True)
        else:
            flash('Failed to send OTP. Try again.', 'danger')
            return render_template('register.html')

    return render_template('register.html')

# -------------------- Login --------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        cursor.execute("SELECT * FROM rdxusers WHERE email = %s", (email,))
        user = cursor.fetchone()

        if user and check_password_hash(user[6], password):
            session['username'] = user[1]
            session['email'] = user[5]
            flash('Login successful!', 'success')
            return redirect(url_for('about'))
        else:
            flash('Invalid email or password.', 'danger')
            return render_template('login.html')

    return render_template('login.html')

# -------------------- Forgot Password --------------------
@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        if 'email' in request.form:
            email = request.form['email']
            cursor.execute("SELECT * FROM rdxusers WHERE email = %s", (email,))
            if cursor.fetchone():
                otp = str(random.randint(100000, 999999))
                session['reset_otp'] = otp
                session['reset_email'] = email
                if send_otp_email(email, otp):
                    flash('OTP sent to your email.', 'info')
                    return render_template('forgot_password.html', otp_sent=True, otp_verified=False)
                else:
                    flash('Failed to send OTP. Try again.', 'danger')
            else:
                flash('Email not found.', 'danger')
            return render_template('forgot_password.html')

        elif 'otp' in request.form:
            if request.form['otp'] == session.get('reset_otp'):
                flash('OTP verified. Please enter new password.', 'success')
                return render_template('forgot_password.html', otp_sent=True, otp_verified=True)
            else:
                flash('Invalid OTP. Try again.', 'danger')
                return render_template('forgot_password.html', otp_sent=True, otp_verified=False)

        elif 'new_password' in request.form:
            new_password = request.form['new_password']
            confirm_password = request.form['confirm_password']

            if new_password != confirm_password:
                flash('Passwords do not match.', 'danger')
                return render_template('forgot_password.html', otp_sent=True, otp_verified=True)

            hashed = generate_password_hash(new_password)
            email = session.get('reset_email')

            cursor.execute("UPDATE rdxusers SET password = %s WHERE email = %s", (hashed, email))
            db.commit()

            session.pop('reset_otp', None)
            session.pop('reset_email', None)

            flash('Password reset successful! Please login.', 'success')
            return redirect(url_for('login'))

    return render_template('forgot_password.html')

# -------------------- Logout --------------------
@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully.', 'info')
    return redirect(url_for('login'))

# -------------------- Run --------------------
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

# initial step
sudo adduser --disabled-password --gecos "" cowrie
sudo passwd cowrie  # set your password for cowrie user
sudo su - cowrie

### login as cowrie user and then only perform these commands

## installation
git clone https://github.com/cowrie/cowrie.git
cd cowrie
---
python3 -m venv cowrie-env
source cowrie-env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
---
cp etc/cowrie.cfg.dist etc/cowrie.cfg
echo "*:*" > etc/userdb.txt
---

# cowrie configuration file path:
nano /home/cowrie/cowrie/etc/cowrie.cfg

# added these new fields in the above config file:
[honeypot]
hostname = ubuntu
auth_none_enabled = false
auth_publickey_enabled = false
auth_password_enabled = true
userdb_enabled = true
userdb_file = etc/userdb.txt

# cowrie restart

cd ~/cowrie
bin/cowrie restart

or

bin/cowrie stop
sleep 2
bin/cowrie start


# see cowrie logs in real time

tail -f ~/cowrie/var/log/cowrie/cowrie.log

# cowrie userpass file location

/home/cowrie/cowrie/etc/userdb.txt

# reset the ssh key

ssh-keygen -R [192.168.100.129]:2222

ssh-keygen -R 192.168.100.130


===========

# applied iptables rule for any SSH (only port 22) traffic to be forwarded onto the cowrie server

sudo iptables -t nat -A PREROUTING -p tcp --dport 22 -j DNAT --to-destination 192.168.100.129:2222

# (optional) if your server has public ip but the cowries is in DMZ or LAN then do this

sudo iptables -t nat -A POSTROUTING -j MASQUERADE


=============


view the iptables rules

sudo iptables -t nat -L -n -v

# Created a custom jail to catch SSH bruteforce

sudo nano /etc/fail2ban/jail.local

add new rules:
------------

[ssh-redirect]
enabled = true
port = ssh
filter = sshd
logpath = /var/log/auth.log
bantime = 600
findtime = 300
maxretry = 3
action = iptables-redirect[name=SSHRedirect, port=22, redirectport=2222, toip=192.168.100.129]

------------
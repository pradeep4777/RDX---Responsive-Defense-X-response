# ip port forwarding to cowrie

sudo sysctl -w net.ipv4.ip_forward=1

# made it persisant

echo "net.ipv4.ip_forward=1" | sudo tee -a /etc/sysctl.conf
sudo sysctl -p


✅ Original (old) Minimal Fail2Ban Config
🔧 1. /etc/fail2ban/jail.local
ini
Copy
Edit
[sshd]
enabled = true
port = ssh
filter = sshd
logpath = /var/log/auth.log
maxretry = 3
bantime = 600
findtime = 300

✅ Added iptables rule for all external SSH traffic to forward on cowrie honeypot
sudo iptables -t nat -A PREROUTING -p tcp -s <attacker_ip> --dport 22 -j DNAT --to-destination 192.168.100.129:2222




==================================================================

# Create the custom action for redirect

sudo nano /etc/fail2ban/action.d/iptables-redirect.conf

----------

[Definition]
actionstart = true
actionstop = true
actioncheck = true

actionban = iptables -t nat -I PREROUTING -s <ip> -p tcp --dport <port> -j DNAT --to-destination <toip>:<redirectport>
actionunban = iptables -t nat -D PREROUTING -s <ip> -p tcp --dport <port> -j DNAT --to-destination <toip>:<redirectport>

----------

sudo systemctl restart fail2ban

# to verify

sudo fail2ban-client status ssh-redirect


# to see the rules inserted

sudo iptables -t nat -L PREROUTING -n -v --line-numbers


==========================================================================================
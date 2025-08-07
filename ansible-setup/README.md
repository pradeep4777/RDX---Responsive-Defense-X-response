# 🛡️ RDX - Automated Incident Response System using Ansible

This project provides an automated playbook to respond to potential attacker IPs using **Ansible**, **Cowrie Honeypot**, **Slack**, **iptables**, and **Nmap**. It is designed to simulate a real-world detection and deception mechanism for educational and cybersecurity training environments.

---

## 🚀 Features

- 🔒 Blocks attacker IP using `iptables`
- 🔁 Redirects attacker to a **Cowrie SSH Honeypot**
- 🔍 Optionally runs **Nmap** scan on the attacker IP
- 🔔 Sends alert notification to **Slack**
- 🧠 Logs all attacker interactions with **Cowrie**

---

## 📁 Project Structure

rdx-ansible/
├── inventory/
│ └── hosts.ini
├── playbooks/
│ └── full_response.yml


---

## 🛠️ Technologies Used

- [Ansible](https://www.ansible.com/)
- [Cowrie Honeypot](https://github.com/cowrie/cowrie)
- [Slack Webhooks](https://api.slack.com/messaging/webhooks)
- iptables
- Nmap

---

## 🧩 Prerequisites

- A Linux VM (tested on Ubuntu 22.04)
- Python3, pip, virtualenv
- Ansible installed (`sudo apt install ansible`)
- Root/sudo access
- Cowrie will run under a **non-root `cowrie` user**
- Optional: Slack webhook URL for alerting

---

## ⚙️ How it Works

1. Attacker attempts to connect via SSH (port 22)
2. `iptables` silently redirects attacker to port 2222 (Cowrie)
3. Cowrie logs every keystroke
4. Slack sends alert (if webhook is configured)
5. Logs are saved under `/home/cowrie/cowrie/var/log/cowrie/`

---

## 🧪 Usage

### 1. Clone Repository

```bash
git clone https://github.com/your-username/rdx-ansible.git
cd rdx-ansible

# Run the Playbook
sudo ansible-playbook -i inventory/hosts.ini playbooks/full_response.yml --extra-vars "attacker_ip=192.168.1.100"

📂 Cowrie Logs Location
/home/cowrie/cowrie/var/log/cowrie/cowrie.log        # Plain text logs
/home/cowrie/cowrie/var/log/cowrie/cowrie.json       # JSON format
/home/cowrie/cowrie/var/log/cowrie/tty/              # Session replay

# 🔐 RDX (Responsive Defense & X-response) – Ansible Automation

This repository contains Ansible configurations for automating cyber threat response in the RDX project. The automation simulates real-world Security Operations Center (SOC) workflows triggered upon detecting threats like brute-force attacks or network scans.

---

## 🚀 Features Automated by Ansible

- 🔒 Block attacker IP using `iptables`
- 🔍 Scan attacker system using `nmap`
- 🎯 Deploy Cowrie honeypot
- 🔔 Send Slack notifications
- ✅ Modular playbook structure for easy reuse and integration

---


---

## 🧰 Prerequisites

Install Ansible on your system:

```bash
sudo apt update
sudo apt install ansible -y

sudo apt install nmap -y

▶️ How to Run
ansible-playbook -i inventory/hosts.ini playbooks/full_response.yml --extra-vars "attacker_ip=192.168.1.100"

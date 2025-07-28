
# 🛡️ RDX: Responsive Defense & X-response

**A proactive, automated, and intelligent security framework that defends, monitors, analyzes, and responds to cyberattacks in real-time.**

---

## 📌 Key Features

- 🔥 Real-time threat detection using **Snort (IDS/IPS)**
- 📦 Log forwarding with **Filebeat**
- 📊 Centralized analysis with **ELK Stack + Wazuh (SIEM)**
- 🤖 Automated incident response using **Ansible**
- 🎯 Attack surface scanning using **Nmap**
- 🕵️‍♂️ Attacker behavior analysis using **Cowrie Honeypot**
- 📈 System health monitoring with **Prometheus**
- 🖼️ Live dashboards with **Grafana & Kibana**
- 🔔 Instant alerts via **Slack / Email**
- 🌐 CI/CD & configuration management via **GitHub**

---

## 📐 Architecture Overview

![Architecture Diagram](./RDX_Workflow_Vertical_Architecture.drawio)

---

## ⚙️ Project Workflow

1. **Attacker initiates** an attack (e.g., brute-force, scan).
2. **Firewall** (iptables/pfSense) filters the traffic.
3. **Server/System** is monitored by:
   - 🕵️ **Snort** (detects threats)
   - 📈 **Prometheus** (tracks system metrics)
4. **Filebeat** forwards logs to **ELK Stack + Wazuh**
5. **Wazuh SIEM** raises alerts on suspicious behavior
6. **Ansible Playbooks** auto-trigger response actions:
   - Block IP
   - Launch **Nmap** against attacker
   - Deploy **Cowrie Honeypot**
7. **Cowrie** traps attackers and logs behavior
8. All data is visualized in:
   - 🖼️ **Grafana** (metrics)
   - 📊 **Kibana** (security logs)
9. **Slack / Email** notifies the **Security Team**
10. **GitHub** stores scripts, configs, and playbooks

---

## 🧰 Tech Stack

- **Network Security**: Snort, Filebeat, Wazuh, pfSense
- **Automation & Response**: Ansible, Cowrie, Nmap
- **Monitoring & Visualization**: Prometheus, Grafana, ELK Stack (Elasticsearch, Logstash, Kibana)
- **Cloud/Infra**: Docker, GitHub, Ubuntu Server
- **Alerting**: Slack, Email Integration

---

## 🚀 Setup Instructions

> This section links to individual setup guides in the repo:

- [`filebeat-setup.md`](./docs/filebeat-setup.md)
- [`snort-setup.md`](./docs/snort-setup.md)
- [`prometheus-node_exporter-setup.md`](./docs/prometheus-node_exporter-setup.md)
- [`grafana-integration.md`](./docs/grafana-integration.md)
- [`ansible-automation.md`](./docs/ansible-automation.md)
- [`cowrie-honeypot-setup.md`](./docs/cowrie-honeypot-setup.md)

---

## 🔐 Security Team Dashboard

Visualize metrics and logs:

| Tool      | Purpose                        |
|-----------|--------------------------------|
| **Kibana**   | Investigate security events   |
| **Grafana**  | Monitor CPU, RAM, Network     |
| **Slack**    | Receive real-time alerts      |
| **GitHub**   | Manage infrastructure scripts |

---


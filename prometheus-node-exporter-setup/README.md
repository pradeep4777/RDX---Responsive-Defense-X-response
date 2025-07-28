# Prometheus + Node Exporter Setup

## Overview

This repository contains configuration files and scripts to install and configure Prometheus and Node Exporter for system monitoring on a Linux machine.

## Usage

1. Clone the repository:
```bash
git clone https://github.com/yourusername/prometheus-node-exporter-setup.git
cd prometheus-node-exporter-setup


2. Install Prometheus:

chmod +x install_prometheus.sh
sudo ./install_prometheus.sh

3. Install Node Exporter:

chmod +x install_node_exporter.sh
sudo ./install_node_exporter.sh

4. Access dashboards:

Prometheus: http://localhost:9090
Node Exporter metrics: http://localhost:9100/metrics
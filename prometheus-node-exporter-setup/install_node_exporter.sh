#!/bin/bash
# Install Node Exporter

cd /opt
wget https://github.com/prometheus/node_exporter/releases/download/v1.8.0/node_exporter-1.8.0.linux-amd64.tar.gz
tar -xvf node_exporter-1.8.0.linux-amd64.tar.gz
sudo cp node_exporter-1.8.0.linux-amd64/node_exporter /usr/local/bin/

# Add systemd service
sudo cp ../node_exporter.service /etc/systemd/system/node_exporter.service

sudo systemctl daemon-reexec
sudo systemctl enable --now node_exporter

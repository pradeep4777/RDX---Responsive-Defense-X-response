#!/bin/bash
# Install Prometheus

sudo useradd --no-create-home --shell /bin/false prometheus

cd /opt
wget https://github.com/prometheus/prometheus/releases/download/v2.50.1/prometheus-2.50.1.linux-amd64.tar.gz
tar -xvf prometheus-2.50.1.linux-amd64.tar.gz
mv prometheus-2.50.1.linux-amd64 prometheus

sudo mv prometheus/prometheus /usr/local/bin/
sudo mv prometheus/promtool /usr/local/bin/
sudo mkdir -p /etc/prometheus
sudo cp -r prometheus/consoles /etc/prometheus
sudo cp -r prometheus/console_libraries /etc/prometheus
sudo cp ../prometheus.yml /etc/prometheus/prometheus.yml

# Create Prometheus service
cat <<EOF | sudo tee /etc/systemd/system/prometheus.service
[Unit]
Description=Prometheus Monitoring
Wants=network-online.target
After=network-online.target

[Service]
User=prometheus
ExecStart=/usr/local/bin/prometheus \\
  --config.file=/etc/prometheus/prometheus.yml \\
  --storage.tsdb.path=/var/lib/prometheus/ \\
  --web.console.templates=/etc/prometheus/consoles \\
  --web.console.libraries=/etc/prometheus/console_libraries

[Install]
WantedBy=multi-user.target
EOF

# Setup directories
sudo mkdir /var/lib/prometheus
sudo chown prometheus:prometheus /var/lib/prometheus

sudo systemctl daemon-reexec
sudo systemctl enable --now prometheus

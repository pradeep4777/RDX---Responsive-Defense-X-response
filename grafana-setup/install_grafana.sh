#!/bin/bash
# Install Grafana on Ubuntu/Debian

sudo apt-get install -y apt-transport-https software-properties-common wget
wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -

sudo add-apt-repository "deb https://packages.grafana.com/oss/deb stable main"
sudo apt-get update
sudo apt-get install grafana -y

# Start and enable Grafana
sudo systemctl daemon-reexec
sudo systemctl enable --now grafana-server

echo "Grafana started. Visit http://localhost:3000"

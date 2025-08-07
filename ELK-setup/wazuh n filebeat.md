
# Wazuh Module for Filebeat
File: /etc/filebeat/modules.d/wazuh.yml

- This module parses Wazuh logs correctly and forwards them to Elasticsearch.

# We enabled it using:
sudo filebeat modules enable wazuh

# Dashboards:

sudo filebeat setup --dashboards
- This loaded default dashboards (including Wazuh if available) into Kibana.

# this changes needs to be done in filebeat for accecing logs from wazuh

filebeat.inputs:
- type: log
  paths:
    - /var/ossec/logs/alerts/alerts.json

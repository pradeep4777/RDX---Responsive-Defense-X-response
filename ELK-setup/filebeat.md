# Output to Elasticsearch
output.elasticsearch:
  hosts: ["http://elk_ip:9200"]
  username: "elastic"
  password: "password"

# Connect to Kibana
setup.kibana:
  host: "http://elk_ip:5601"
  username: "kibana_system"
  password: "password"

# Enable Apache logs if needed
filebeat.inputs:
- type: log
  enabled: true
  paths:
    - /var/log/apache2/*.log

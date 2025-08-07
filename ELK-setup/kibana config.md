at the end of the /etc/kibana/kibana.yml
- copy this file and comment everything else if present

----------------------------------------------------------------------------------------------------------------

### >>>>>>> BACKUP END: Kibana interactive setup (2025-07-28T07:02:04.126Z)

# This section was automatically generated during setup.
server.host: "0.0.0.0"

elasticsearch.hosts: ["<ELK IP>:9200"]
elasticsearch.username: "kibana_system"
elasticsearch.password: "password"

logging.appenders.file.type: file
logging.appenders.file.fileName: /var/log/kibana/kibana.log
logging.appenders.file.layout.type: json
logging.root.appenders: [file]

pid.file: /run/kibana/kibana.pid
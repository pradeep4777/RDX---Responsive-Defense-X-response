nano /etc/kibana/kibana.yml
-----------------------------

server.host: "0.0.0.0"

elasticsearch.hosts: ["http://<host_IP>:9200"]
elasticsearch.username: "kibana_system"
elasticsearch.password: "<password>"

logging.appenders.file.type: file
logging.appenders.file.fileName: /var/log/kibana/kibana.log
logging.appenders.file.layout.type: json
logging.root.appenders: [default, file]

pid.file: /run/kibana/kibana.pid

=================================================
in elk machine we have to create a user named kibana in elastic with kibana user

sudo /usr/share/elasticsearch/bin/elasticsearch-users useradd kibanauser -p yourStrongPassword -r kibana_admin

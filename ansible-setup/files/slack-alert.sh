#!/bin/bash
ATTACKER_IP="$1"
WEBHOOK_URL="https://hooks.slack.com/services/XXXX/YYYY/ZZZZ"

curl -X POST -H 'Content-type: application/json' \
--data "{\"text\":\"🚨 RDX Alert: Attacker IP $ATTACKER_IP has been blocked, scanned, and honeypot deployed.\"}" \
$WEBHOOK_URL

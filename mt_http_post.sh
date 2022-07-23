#/bin/bash

curl -X POST 127.0.0.1:7581 \
 -H "Content-Type: application/json" \
 -d "@mt_input.json"

#!/usr/bin/python

# Marcel Timm, RhinoDevel, 2022jul25

# curl -X POST 127.0.0.1:7581 \
#  -H "Content-Type: application/json" \
#  -d "@demo.json"

import config
import subprocess

INTENT_FILE = 'intent.json'

def send():
    c = config.get()
    d = None

    with open(INTENT_FILE) as f:
        d = f.read()

    subprocess.run([
            'curl',
            '-X', 'POST',
            c['addr'] + ':' + str(c['port']),
            '-H', '"Content-Type: application/json"',
            '-d', d
        ])

if __name__ == "__main__":
    send()
    print()
#!/usr/bin/python

# Marcel Timm, RhinoDevel, 2022jul29

import subprocess

import config
from timer import timer

def _on_alert(msg):
    """Call this function for each timer that is due."""

    c = config.get()
    a = [
            'curl',
            '-X', 'POST',
            'http://' + c['rhasspy_addr'] + ':' + str(c['rhasspy_port'])
                + '/api/text-to-speech?play=true',
            '-H', 'accept: audio/wav',
            '-H', 'Content-Type: text/plain',
            '-d', msg
        ]

    subprocess.run(
        a,
        stdin = subprocess.DEVNULL,
        stdout = subprocess.DEVNULL,
        stderr = subprocess.DEVNULL)

if __name__ == "__main__":
    timer.exec(_on_alert)

#!/usr/bin/python

# Marcel Timm, RhinoDevel, 2022jul29

from timer import timer

def _on_alert(msg):
    """Call this function for each timer that is due."""

    print('ALERT: ' + '"' + msg + '"!') # TODO: Replace with something that makes sense!

    #curl -X POST "http://pi4.fritz.box:12101/api/text-to-speech?play=true" -H  "accept: audio/wav" -H  "Content-Type: text/plain" -d "Ding dong ding dong ding! Der Teimer ist abgelaufen."


if __name__ == "__main__":
    timer.exec(_on_alert)

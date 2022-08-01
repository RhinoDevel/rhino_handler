#!/usr/bin/bash

# Marcel Timm, RhinoDevel, 2022aug01

(crontab -l ; echo "* * * * * ~/rhino_handler/timer_exec.py") | crontab -

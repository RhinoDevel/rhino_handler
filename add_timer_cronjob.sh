#!/usr/bin/bash

# Marcel Timm, RhinoDevel, 2022aug01

# Hard-coded working directory (see config.py):
#
(crontab -l ; echo "* * * * * ~/rhino_handler/timer_exec.py") | crontab -

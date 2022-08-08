#!/usr/bin/bash

# Marcel Timm, RhinoDevel, 2022aug01

# Hard-coded working directory:
#
(crontab -l ; echo "* * * * * cd ~/rhino_handler && ./timer_exec.py") | crontab -

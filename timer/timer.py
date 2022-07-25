#!/usr/bin/python

# Marcel Timm, RhinoDevel, 2022jul25

import json
import random
import os
from time import time, localtime, sleep

from config import get

FILE_NAME = 'timer.json'
FILE_RUNS_LOCK = 'timer.lock'

def _try_lock_running():
    """Tries to set is-running-lock. Returns, if successful or not."""

    try:
        with open(FILE_RUNS_LOCK, 'x'):
            return True
    except:
        return False # File seems to already exist.

def _unlock_running():
    """Unlocks the is-running-lock."""

    os.remove(FILE_RUNS_LOCK)

def _wait_for_lock_running():
    while not _try_lock_running(): # TODO: Add a timeout and exception!
        sleep(0.5) # seconds (at least).

def _get_default():
    return {}

def _try_load():
    try:
        with open(FILE_NAME) as f:
            return json.loads(f.read())
    except:
        return None

def _save(o):
    with open(FILE_NAME, 'w') as f:
        f.write(json.dumps(o))

def _set(o):
    _save(o)

def _get():
    ret_val = _try_load()
    if ret_val is None:
        ret_val = _get_default()

    return ret_val

def _get_unique_id(o):
    ret_val = None
    
    while True:
        ret_val = str(random.randint(10000000, 99999999))
        if(ret_val not in o):
            break

    return ret_val

def _add(msg, timestamp):
    """This is to be run from the script that adds timer events.
    
    This is normally the HTTP server.
    It may runs in parallel with this same script started by a timer's cron job,
    hence the locking mechanism.
    """

    _wait_for_lock_running()

    o = _get()
    entry_id = _get_unique_id(o)
    ret_val = localtime(timestamp)

    o[entry_id] = {
            'timestamp': timestamp,
            'msg': msg        
        }

    _set(o)

    _unlock_running()

    return ret_val

def add_minutes(msg, minutes):
    return _add(msg, time() + 60.0 * minutes)

def add_hours(msg, hours):
    return add_minutes(msg, 60.0 * hours)

def exec():
    """This is to be run by a cron job.
    
    May be running in parallel with some add function, hence the lock mechanism.
    """

    _wait_for_lock_running()

    o = _get()

    # TODO: Implement!

    _set(o)

    _unlock_running()

if __name__ == "__main__":
    exec()
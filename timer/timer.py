#!/usr/bin/python

# Marcel Timm, RhinoDevel, 2022jul25

import json
import random
from time import time, localtime

from config import get

FILE_NAME = 'timer.json'

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
    o = _get() # Should work, even if other process [see exec()] accesses this.
    entry_id = _get_unique_id(o)
    ret_val = localtime(timestamp)

    o[entry_id] = {
            'timestamp': timestamp,
            'msg': msg        
        }

    _set(o) # TODO: Can this be a problem [see exec()]?!

    return ret_val

def add_minutes(msg, minutes):
    return _add(msg, time() + 60.0 * minutes)

def add_hours(msg, hours):
    return add_minutes(msg, 60.0 * hours)

def exec():
    o = _get() # Should work, even if other process [see _add()] accesses this.

    # TODO: Implement!

    _set(o) # TODO: Can this be a problem [see _add()]?!

if __name__ == "__main__":
    exec()
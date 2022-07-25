
# Marcel Timm, RhinoDevel, 2022jul25

import json

FILE_NAME = 'config.json'

def _get_default():
    return {
        'addr': 'pi4.fritz.box', # HTTP server's address.
        'port': 7581             # HTTP server's port.
    }

def _try_load():
    try:
        with open(FILE_NAME) as f:
            return json.loads(f.read())
    except:
        return None

def _save(o):
    with open(FILE_NAME, 'w') as f:
        f.write(json.dumps(o))

def set(o):
    _save(o)

def get():
    ret_val = _try_load()
    if ret_val is None:
        ret_val = _get_default()

    return ret_val


# Marcel Timm, RhinoDevel, 2022jul17

import os
import importlib
import importlib.util

import responder.intents

INTENT_UNKNOWN = 'unknown' # Default for unknown intent.
ERR_MSG_ON_EXCEPTION = 'Entschuldigung, es ist ein Ausnahmefehler aufgetreten.'

FILE_LAST_RESPONSE = 'last_response.txt'
FILE_RUNS_LOCK     = 'responder.lock'
#
# Will be saved to root folder inside docker container with Rhasspy 2.5.1 (is
# that OK?).

def try_lock_running():
    """Tries to set is-running-lock. Returns, if successful or not."""

    try:
        with open(FILE_RUNS_LOCK, 'x'):
            return True
    except:
        return False # File seems to already exist.

def unlock_running():
    """Unlocks the is-running-lock."""

    os.remove(FILE_RUNS_LOCK)

def save_last_response(s):
    """
    Tries to save the given string to the last-response file. Nothing happens,
    if saving fails.
    """

    try:
        with open(FILE_LAST_RESPONSE, 'w') as f:
            f.write(s)
    except:
        pass

def load_last_response():
    """Tries to load the last response from file. Returns None, if not found."""
 
    ret_val = None
    l = None

    try:
        with open(FILE_LAST_RESPONSE) as f:
            l = f.readlines()
            if len(l) == 1:
                ret_val = l[0]
    except:
        pass

    return ret_val

def get_module_path(intent):
    return responder.intents.__name__ + '.' + intent.lower()

def exec_without_lock(intent, params):
    """
    Get intent (name) and parameters (dictionary), return response string.
    Augments given parameters object with last-response property.
    Additionally saves response to last-response file.
    """

    ret_val = None
    module_path = get_module_path(intent)

    if(importlib.util.find_spec(module_path) is None):
        module_path = get_module_path(INTENT_UNKNOWN)

    # Augmenting parameters object with last-response property:
    #
    params['last_response'] = load_last_response()

    ret_val = importlib.import_module(module_path).exec(params)

    save_last_response(ret_val)

    return ret_val

def exec(intent, params):
    ret_val = None

    if not try_lock_running():
        ret_val = '' # Returns an empty string, if lock cannot be acquired!
    else:
        try:
            ret_val = exec_without_lock(intent, params)
        except:
            ret_val = ERR_MSG_ON_EXCEPTION

        unlock_running()

    return ret_val

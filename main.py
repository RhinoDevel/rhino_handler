#!/usr/bin/python3

# Marcel Timm, RhinoDevel, 2022jul16

# *** Some notes ***
#
# - Create a gzipped tarball from a folder:
#
#   tar cvzf TimmIntentHandler.tar.gz ./TimmIntentHandler
#
# - Execute BASH "inside" docker environment:
#
#   docker exec -it rhasspy bash

import json
import os
import sys

import responder

# Will be saved to root folder inside docker container (is that OK?):
#
FILE_LAST_RESPONSE = 'last_response.txt'
FILE_RUNS_LOCK     = 'rhino_handler.lock'

def send_output(s):
    """Send the output of this intent handler."""

    print(s)

def get_output(obj):
    """Create and return the output string of this handler from given object."""

    return json.dumps(obj)

def add_response(response, obj):
    """Add the response given to the input/output object that is also given."""

    obj['speech'] = {'text': response}

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

def get_params(obj):
    """Extract and return (intent) parameters from given object."""

    ret_val = {}

    ret_val['last_response'] = load_last_response()

    # TODO: Implement adding parameters from input object!

    return ret_val

def get_intent(obj):
    """Extract and return intent (name) from given object."""

    return obj['intent']['name']

def get_obj(s):
    """Create and return input/output object from given string."""

    return json.loads(s)    

def retrieve_input():
    """Return string which is the input to this intent handler."""

    return sys.stdin.read()

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

def exec_with_obj(obj):
    """ 
    Get input from parameter (object) and augment that object with the 
    response. Also saves that response as last response to a file.
    """

    intent = get_intent(obj)
    params = get_params(obj)
    response = responder.exec(intent, params)

    add_response(response, obj)
    
    save_last_response(response)

def exec_with_str(input_str):
    """Get input from parameter (string) and return response as string."""

    ret_val = None
    obj = get_obj(input_str)

    exec_with_obj(obj)

    ret_val = get_output(obj)

    return ret_val

def exec_with_std():
    """Retrieve input from stdin and send response to stdout."""

    input_str = retrieve_input()
    output_str = exec_with_str(input_str)

    send_output(output_str)

def main():
    if not try_lock_running():
        return # No return value at all. Is this OK?

    try:
        exec_with_std()
    except:
        pass # Maybe no return value at all. Is this OK?

    unlock_running()

main()

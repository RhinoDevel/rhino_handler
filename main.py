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
import sys

import responder

FILE_LAST_RESPONSE = 'last_response.txt'

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
    """Tries to save the given string to the last response file."""

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

def main():
    # TODO: Make this thread-safe/atomic!

    input_str = retrieve_input()
    obj = get_obj(input_str)
    intent = get_intent(obj)
    params = get_params(obj)
    response = responder.exec(intent, params)
    output_str = None

    add_response(response, obj)
    output_str = get_output(obj)

    save_last_response(response)

    send_output(output_str)    

main()

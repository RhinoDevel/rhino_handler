#!/usr/bin/python3

# Marcel Timm, RhinoDevel, 2022jul16

# *** Some notes ***
#
# - Execute BASH "inside" docker environment:
#
#   docker exec -it rhasspy bash

import json
import sys

from responder import responder

def get_params(obj):
    """Extract and return (intent) parameters from given object."""

    ret_val = {}

    # TODO: Implement adding parameters from input object!

    return ret_val

def exec_with_obj(obj):
    """ 
    Get input from parameter (object) and augment that object with the 
    response.
    """

    intent = obj['intent']['name']
    params = get_params(obj)

    response = responder.exec(intent, params)
    #
    # (augments parameters object)

    obj['speech'] = {'text': response} # Augments in-/output obj. with response.

def exec_with_str(input_str):
    """Get input from parameter (string) and return response as string."""

    ret_val = None
    obj = json.loads(input_str)

    exec_with_obj(obj)

    ret_val = json.dumps(obj)

    return ret_val

def exec_with_std():
    """Retrieve input from stdin and send response to stdout."""

    input_str = sys.stdin.read()
    output_str = exec_with_str(input_str)

    print(output_str)

if __name__ == "__main__":
    exec_with_std()

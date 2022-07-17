
# Marcel Timm, RhinoDevel, 2022jul17

import os.path
import importlib
import importlib.util
import intents

def get_module_path(intent):
    return intents.__name__ + '.' + intent.lower()

def exec(intent, params):
    """Get intent (name) and parameters (dictionary), return response string """

    module_path = get_module_path(intent)

    if(importlib.util.find_spec(module_path) is None):
        module_path = get_module_path('unknown') # Default for unknown intent.

    return importlib.import_module(module_path).exec(params)

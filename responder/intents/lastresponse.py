
# Marcel Timm, RhinoDevel, 2022jul18

import mt.str

def exec(params):
    if params['last_response'] is None:
        return 'Ich habe doch noch gar nichts gesagt!'
    
    assert(mt.str.is_nonwhitespace(params['last_response']))

    return params['last_response']


# Marcel Timm, RhinoDevel, 2022jul17

import random

def exec(params):
    return random.choice([
            'Was meinst Du?',
            'Ich habe das nicht verstanden.',
            'Keine Ahnung, was Du möchtest.',
            'Wie bitte?',
            'Dazu kann ich nichts sagen.',
            'Das verstehe ich leider nicht.'
        ])

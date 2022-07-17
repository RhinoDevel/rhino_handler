
# Marcel Timm, RhinoDevel, 2022jul17

from datetime import datetime

def exec(params):
    now = datetime.now()
    
    return 'Es ist %s Uhr %s' % (now.strftime('%H'), now.minute)

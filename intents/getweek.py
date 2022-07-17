
# Marcel Timm, RhinoDevel, 2022jul17

from datetime import datetime

def exec(params):
    now = datetime.now()
    
    return 'Wir haben die %s. Woche des Jahres' % now.strftime('%W')

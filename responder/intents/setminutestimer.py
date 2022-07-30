
# Marcel Timm, RhinoDevel, 2022jul30

from time import time, localtime

from timer import timer

ALERT_TEXT = 'Ding dong ding, piep piep piep, ding dong ding.'

def exec(params):
    ret_val = None
    now_time = localtime(time())
    minutes = params['slots']['minutes'] # Better use entitites property?
    due_time = None
    msg = ALERT_TEXT + ' Der'

    if minutes == 1:
        msg += ' eine Minute'
    else:
        msg += ' ' + str(minutes) + ' Minuten'
    msg += (' Teimer von'
            + ' ' + str(now_time.tm_hour) + ' Uhr ' + str(now_time.tm_min)
            + ' ist abgelaufen.')

    due_time = timer.add_minutes(msg, minutes)

    ret_val = ('Um ' + str(due_time.tm_hour) + ' Uhr ' + str(due_time.tm_min)
        + ' wird der Teimer ablaufen und die Benachrichtigung erfolgen.')

    return ret_val

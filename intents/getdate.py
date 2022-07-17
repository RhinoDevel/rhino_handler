
# Marcel Timm, RhinoDevel, 2022jul17

from datetime import datetime
import random

# Locale does not seem to be changeable (seems to be a Rhasspy / docker problem..):
#
DE_WEEKDAYS = [
        'Montag',
        'Dienstag',
        'Mittwoch',
        'Donnerstag',
        'Freitag',
        random.choice(['Sonnabend', 'Samstag']),
        'Sonntag'
    ]

DE_MONTHS = [
        'Januar',
        'Februar',
        'März',
        'April',
        'Mai',
        'Juni',
        'Juli',
        'August',
        'September',
        'Oktober',
        'November','Dezember'
    ]

def exec(params):
    now = datetime.now()
    
    return 'Heute ist %s, der %s. %s %s' % (
            DE_WEEKDAYS[now.weekday()],
            now.strftime('%d'),
            DE_MONTHS[now.month - 1], now.strftime('%Y')
        )

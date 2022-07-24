
# Marcel Timm, RhinoDevel, 2022jul24

from audio import player

LOCATION = 'http://www.c64.com:8000'

def exec(params):
    player.play(LOCATION)
    return ''

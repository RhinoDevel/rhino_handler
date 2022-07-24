
# Marcel Timm, RhinoDevel, 2022jul24

import subprocess

DEFAULT_STEP = 5 # percent

def set_from_str(s):
    """
    Set master volume to value given as string (can be something like '5%-"
    to e.g. lower the volume, too - see amixer man. page).
    """

    subprocess.run(
            ['amixer', '-M', '-c0', 'set', 'Headphone', s],
            stdin = subprocess.DEVNULL,
            stdout = subprocess.DEVNULL,
            stderr = subprocess.DEVNULL
        )

def get_str(percent):
    return str(percent) + '%'

def decrease_by(percent):
    set_from_str(get_str(percent) + '-')

def increase_by(percent):
    set_from_str(get_str(percent) + '+')

def set(percent):
    set_from_str(get_str(percent))

def increase():
    increase_by(DEFAULT_STEP)

def decrease():
    decrease_by(DEFAULT_STEP)
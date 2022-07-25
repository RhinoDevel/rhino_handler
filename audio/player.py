
# Marcel Timm, RhinoDevel, 2022jul23

import os
import signal
import subprocess

FILE_RUNS_PID = 'audio_player.pid'

def delete_running_pid():
    """Removes the running-PID file. Does not matter, if file exists or not."""

    try:
        os.remove(FILE_RUNS_PID)
    except FileNotFoundError:
        pass

def save_running_pid(pid):
    """Tries to save the given process ID to the running-PID file.
    
    Throws an exception, if saving fails (e.g. file already exists).
    """

    with open(FILE_RUNS_PID, 'x') as f:
        f.write(str(pid))

def load_running_pid():
    """Tries to load the process ID of a currently running player from file.
    
    Returns None, if not found, which is interpreted as no audio player running.
    """
 
    ret_val = None
    l = None

    try:
        with open(FILE_RUNS_PID) as f:
            l = f.readlines()
            if len(l) == 1:
                ret_val = l[0]
                ret_val = int(ret_val)
    except:
        pass

    return ret_val

def stop():
    pid = load_running_pid()
    if pid is None:
        return # Nothing to do.

    os.kill(pid, signal.SIGTERM)

    delete_running_pid() 

def play(location):
    process = None

    stop()

    process = subprocess.Popen(
            ['mpv', location],
            start_new_session = True,
            stdin = subprocess.DEVNULL,
            stdout = subprocess.DEVNULL,
            stderr = subprocess.DEVNULL
        )

    save_running_pid(process.pid)

    # TODO:
    #
    # The player application process gets terminated via SIGTERM and the process
    # stays around as zombie.
    #
    # The cause of that seems to be that the Popen object is not really given to
    # the garbage collector until the whole Python script exits.
    #
    # How can we improve this (to avoid more and more zombie processes being
    # around and maybe even pollute the memory with "zombie" Popen objects?)
    # 
    process = None
                   
# There may be a PID file from before last reboot, just delete it:
#
delete_running_pid()
import platform
import os
import subprocess
import time
from speaker import Speaker

def ping(host):
    """
    Returns True if host responds to a ping request
    """

    # Ping parameters as function of OS
    ping_str = "-n 1" if  platform.system().lower()=="windows" else "-c 1"
    # Ping
    FNULL = open(os.devnull, 'w')
    response = subprocess.run("ping "+ping_str+" "+host, stdout=FNULL)
    return response.returncode == 0

speaker = Speaker()
previously_connected = False

print("Monitoring phone connection")

try:
    while True:
        result = ping("127.0.0.1")
        if result == True and previously_connected == False:
            print("Phone connected")
            speaker.read('Welcome home, Nick.')
            previously_connected = True
        elif result == False and previously_connected == True:
            print("Your phone isn't connected")
            speaker.read('Goodbye, Nick.')
            previously_connected = False
        time.sleep(5)
except KeyboardInterrupt:
    print('Script stopped by user')

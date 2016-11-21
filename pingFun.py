import platform
import os
import subprocess
import time
import argparse
from speaker import Speaker
from config_handler import ConfigHandler

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

configurator = ConfigHandler()

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--config', help='Configurate the script',
                    action='store_true', default=False)
args = parser.parse_args()

if args.config:
    configurator.menu()

config = configurator.get_config()

speaker = Speaker()
previously_connected = False

print("Monitoring phone connection")

try:
    while True:
        result = ping(config['PhoneIp'])
        if result == True and previously_connected == False:
            print("Phone connected")
            speaker.read('Welcome home, ' + config['UserName'])
            previously_connected = True
        elif result == False and previously_connected == True:
            print("Your phone isn't connected")
            speaker.read('Goodbye, ' + config['userName'])
            previously_connected = False
        time.sleep(5)
except KeyboardInterrupt:
    print('Script stopped by user')

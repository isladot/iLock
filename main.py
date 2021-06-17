import os

import ctypes
import platform
import threading
import subprocess
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

IP = os.environ.get("PHONE_IP")

def ping_phone():
  # Pings amount param.
  param = '-n' if platform.system().lower() == 'windows' else '-c'
  # Ping command.
  command = ['ping', param, '1', IP]
  # Pinging Phone. 
  result = subprocess.call(command) == 0
  # Get and parse current time.
  now = datetime.now().strftime("%d/%m/%Y - %H:%M:%S")

  # Check if Phone replied.
  if(result):
    # Log phone detection.
    print(f'{now}: Phone detected.')
  else:
    # Log phone undetection.
    print(f'{now}: Phone not detected, locking computer.')
    # Lock computer.
    lock_windows()
    return

  # Periodically ping Phone.
  threading.Timer(20, ping_phone).start()

def lock_windows():
  ctypes.windll.user32.LockWorkStation()

def main():
  ping_phone()

main()

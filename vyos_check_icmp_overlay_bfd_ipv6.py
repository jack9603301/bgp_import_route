#!/usr/bin/env python3
from __future__  import print_function
import subprocess
import threading
import time

def is_reachable(ip):
    if subprocess.call(["ping", "-W", "1", "-c", "1", ip])==0:
        return True
    else:
        return False

def loop_main():
    if(is_reachable("fc00:320:f1cd:2::1") == False):
        subprocess.call(["ip", "link", "set", "dev", "tun2", "down"])
        #You must exit first to ensure that the routing table is not cleared when multiple redundancy is invalid
        return
    else:
        subprocess.call(["ip", "link", "set", "dev", "tun2", "up"])
    if(is_reachable("fc00:330:f1cd:2::1") == False):
        subprocess.call(["ip", "link", "set", "dev", "tun3", "down"])
    else:
        subprocess.call(["ip", "link", "set", "dev", "tun3", "up"])

if __name__ == "__main__":
    while True:
      loop_main()
      time.sleep(1)

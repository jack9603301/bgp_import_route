#!/usr/bin/env python3
from __future__  import print_function
import subprocess
import threading

def is_reachable(ip):
    if subprocess.call(["ping", "-W", "1", "-c", "1", ip])==0:
        return True
    else:
        return False

def loop_main():
    if(is_reachable("192.168.10.1") == False):
        subprocess.call(["ip", "link", "set", "dev", "tun0", "down"])
        #You must exit first to ensure that the routing table is not cleared when multiple redundancy is invalid
        return
    else:
        subprocess.call(["ip", "link", "set", "dev", "tun0", "up"])
    if(is_reachable("192.168.30.1") == False):
        subprocess.call(["ip", "link", "set", "dev", "tun1", "down"])
    else:
        subprocess.call(["ip", "link", "set", "dev", "tun1", "up"])

if __name__ == "__main__":
    loop_main()

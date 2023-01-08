#! /usr/bin/env python3

import json
import urllib3

def main():
    url = "https://api.bgpview.io/asn/36459/prefixes"
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    jsondata = json.loads(r.data)
    values =  json.dumps(jsondata, sort_keys=True, indent=4, separators=(',', ': '))
    print(jsondata)
    
    print("DECODE>")

    for dict in jsondata["data"]["ipv4_prefixes"]:
        print("-------------------")
        print(dict["prefix"])
        print("-------------------")
    pass

if __name__ == "__main__":
    main()
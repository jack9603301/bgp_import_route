#! /usr/bin/env python3

import json
import urllib3

def get_ips(ASN_set, type):
    if type == "ipv4":
        type = "ipv4_prefixes"
    elif type == "ipv6":
        type = "ipv6_prefixes"
    
    result = {}
    
    for ASN in ASN_set:
        url = f"https://api.bgpview.io/asn/{ASN}/prefixes"
        http = urllib3.PoolManager()
        r = http.request('GET', url)
        jsondata = json.loads(r.data)
        only_asn_ips = jsondata["data"][type]
        result.update({ASN: only_asn_ips})

    return result

def main():
    ips = get_ips([15169,36459,54113,32934,3356,62041,4826,16276,22611,19679,34282,16509,8075,14061,58182,64050,38197,206281,34240,13414,13335,24940,24572,23816,20446],"ipv4")
    values =  json.dumps(ips, sort_keys=True, indent=4, separators=(',', ': '))
    print(values)
    
    print("INSTALL ROUTE>")
    for key,value in ips.items():
        ASN = key
        for dict in value:
            prefix = dict["prefix"]
            print(f"ip route {prefix} enp1s0 label AS{ASN}")

def test_main():
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
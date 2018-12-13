import fileopener
import re
import ipaddress
import json
import sys

def valid_ip(address):
    try: 
        print (ipaddress.ip_network(address))
        return True
    except:
        return False

#routescan=fileopener.fileread('routefile.txt')
with open('routefile.txt',encoding='utf-8') as data:
    resp_dict=json.loads(data.read())
    #routes learnt from the router
    cidrblocklearnt=resp_dict['route-information'][0]['route-table'][0]['rt'][0]['rt-destination'][0]['data']
    #nexthopdetail=resp_dict['route-information'][0]['route-table'][0]['rt'][0]['rt-destination'][0]['nh'][0]['via']
    subnetextract=re.findall(r'/[0-9]{1,3}',cidrblocklearnt)
    hello=re.findall(r'[0-9]{1,3}',subnetextract[0])
    hello1=int(hello[0])
    print(hello1)
    IPextract=re.findall(r'[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}',cidrblocklearnt)
    print(subnetextract)
    print(IPextract)
   # print (resp_dict['route-information'][0]['route-table'][0]['rt'][0]['rt-destination'][0]['data'])
    print (resp_dict['route-information'][0]['route-table'][0]['rt'][0]['rt-entry'][0]['nh'][0]['via'][0]['data'])



    







import progfunctions
import re
import json
import sys

#routescan=fileopener.fileread('routefile.txt')
with open('routefile.txt',encoding='utf-8') as data:
    resp_dict=json.loads(data.read())
    #routes learnt from the router
    cidrblocklearnt=resp_dict['route-information'][0]['route-table'][0]['rt'][0]['rt-destination'][0]['data']
    #nexthopdetail=resp_dict['route-information'][0]['route-table'][0]['rt'][0]['rt-destination'][0]['nh'][0]['via']
    progfunctions.subnetextract(cidrblocklearnt)
   # progfunctions.subnetgenerator(ipsubnet)
        
    ipextract=re.findall(r'[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}',cidrblocklearnt)
    print(ipextract)
   # print (resp_dict['route-information'][0]['route-table'][0]['rt'][0]['rt-destination'][0]['data'])
    print (resp_dict['route-information'][0]['route-table'][0]['rt'][0]['rt-entry'][0]['nh'][0]['via'][0]['data'])



    







import progfunctions
import re
import json
import sys
i=0
with open('routefile.txt',encoding='utf-8') as data:
    resp_dict=json.loads(data.read())
    while True:
        if resp_dict is None:
            break
        else:
            #print(resp_dict['route-information'][0]['route-table'][0]['rt'][0]['rt-destination']['data'])
            cidrblocklearnt=resp_dict['route-information'][0]['route-table'][0]['rt'][i]['rt-destination'][0]['data']#routes learnt from the router
            print (cidrblocklearnt)
        #nexthopdetail=resp_dict['route-information'][0]['route-table'][0]['rt'][0]['rt-destination'][0]['nh'][0]['via']
            ipsubnets=progfunctions.subnetextract(cidrblocklearnt)
#            with open('ipsubnetsfile.txt','a',encoding='utf-8') as breakupsubnets:
#                breakupsubnets.write(ipsubnets)
            print (ipsubnets)
            i=i+1
            if i >= len(resp_dict['route-information'][0]['route-table'][0]['rt']):
                break
        
        # print (resp_dict['route-information'][0]['route-table'][0]['rt'][0]['rt-destination'][0]['data'])
        # print (resp_dict['route-information'][0]['route-table'][0]['rt'][0]['rt-entry'][0]['nh'][0]['via'][0]['data'])



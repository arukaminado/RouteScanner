import fileopener
import re
import ipaddress

def valid_ip(address):
    try: 
        print (ipaddress.ip_network(address))
        return True
    except:
        return False


routescan=fileopener.fileread('routefile.txt')
for p,q in enumerate(routescan):
    routescan[p]=q.strip()

for j in routescan:
#    routescanclean=list(map(str.strip,j))
    ipaddressstrip=re.findall(r'[0-9]+(?:\.)[0-9]+(?:\.)[0-9]+(?:\.)+.....',j)
    print (ipaddressstrip)
#for i in routescanclean:
 #   testIP= valid_ip(i)
    
        


import ipaddress
import re

#Read only file open 
def fileread(filename):
    with open (filename,"r+") as newfile:
        newfile.seek(0)
        listelement=newfile.readlines()
        return listelement
    newfile.close()

#Check for Valid IP Address
def valid_ip(address):
    try: 
        print (ipaddress.ip_network(address))
        return True
    except:
        return False

#Return the Int Value of the Subnet
def subnetextract(subnetvalue):
    subnetextract=re.findall(r'/[0-9]{1,3}',subnetvalue) #extract the subnet from the list
    subnetlist=re.findall(r'[0-9]{1,3}',subnetextract[0]) #extract the subnet without the /
    subnetint=int(subnetlist[0]) #convert the subnet to integer for the loop
    ipextract=re.findall(r'[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}',subnetvalue) #extract the IP address from the list
    ipextractstr=str(ipextract[0]) #convert the IP address into a string value
    ipsubnets=[] #blank list to store the IP subnets range viz. 10.10.10.10/20 >> List value 10.10.10.10/21, 10.10.10.10/22, 10.10.10.10/23 & 10.10.10.10/24
    prefix_subnets=list(ipaddress.ip_network(subnetvalue).subnets())
    print(type(prefix_subnets))
    print(prefix_subnets)
    for x_value in prefix_subnets:
            print(x_value.with_prefixlen)
    while subnetint<=32:
        if(subnetint>8)==True and (subnetint<=32)==True:
            subnetstr=str(subnetint)
            with open('ipsubnetsfile.txt','a',encoding='utf-8') as breakupsubnets:
                breakupsubnets.write(ipextractstr+'/'+subnetstr+'\n')
            ipsubnets.append(ipextractstr+'/'+subnetstr)
            subnetint=subnetint+1
    return ipsubnets
            

#Return the subnets of a CIDR
def subnetgenerator(cidrblock):
    while cidrblock<25:
        if (cidrblock>8)==True and (cidrblock<25)==True:
            print (cidrblock)
            cidrblock=cidrblock+1








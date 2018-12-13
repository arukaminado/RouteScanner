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
    subnetextract=re.findall(r'/[0-9]{1,3}',subnetvalue)
    print(subnetextract)
    subnetlist=re.findall(r'[0-9]{1,3}',subnetextract[0])
    subnetint=int(subnetlist[0])
    ipextract=str(re.findall(r'[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}',subnetvalue))
    while subnetint<25:
        if(subnetint>8)==True and (subnetint<25)==True:
            subnetconvert[subnetint]=str(subnetint)
            print(ipextract+subnetconvert[subnetint])
            subnetint=subnetint+1

    #return(subnetint)

#Return the subnets of a CIDR
def subnetgenerator(cidrblock):
    while cidrblock<25:
        if (cidrblock>8)==True and (cidrblock<25)==True:
            print (cidrblock)
            cidrblock=cidrblock+1








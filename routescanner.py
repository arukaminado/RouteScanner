import fileopener
import re
routescan=fileopener.fileread('routefile.txt')
for i in routescan:
    b= re.search(r"(.+?)+(\d) +(.+?)\s{2,}(\w)*",i)
    print (b)

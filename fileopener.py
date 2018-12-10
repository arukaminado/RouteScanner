#Read only file open 
def fileread(filename):
    with open (filename,"r+") as newfile:
        newfile.seek(0)
        listelement=newfile.readlines()
        return listelement
    newfile.close()


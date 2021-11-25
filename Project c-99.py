import os
import shutil

path=input("enter path")
pathStatus=os.path.exists(path)

if(pathStatus):
    for root_folder, folders, files in os.walk(path):
        
        removefolder(root_folder)
        for folder in folders:
            removefolder(folder)
        for file in files:
            removefile(file)
else:
    print("path doesn't exist")


def removefolder(path):
    pathStatus=os.path.exists(path)
    if(pathStatus):
        shutil.rmtree(path)
    else:
        print("path doesn't exist")
def removefile(path):
    pathStatus=os.path.exists(path)
    if(pathStatus):
        os.remove(path)
    else:
        print("path doesn't exist")


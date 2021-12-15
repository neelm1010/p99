import os
import time

path  = input("Enter the path:")
days = int(input("Till how many days do you want to remove files:"))
days = time.time() - days * 24 * 60 * 60 


path_exists = os.path.exists(path)
ctime = os.stat(path).st_ctime


if(path_exists):
    list = os.walk(path)
    for subfolder,folders,files in list:

        if days > ctime:
            os.remove(folders)
            os.remove(files)
            os.remove(subfolder)
        


else: 
    print("Error path not found")
    time.sleep(4)
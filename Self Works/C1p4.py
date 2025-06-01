# WAP to print the contents a directory using OS module . 

import os

directory_path ='/'

contents = os.listdir(directory_path)

for item in contents:
    print (item)
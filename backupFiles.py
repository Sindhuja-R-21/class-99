import os
import shutil

source=input("Enter the Source Folder Name:- ")
destination=input("Enter the Destination Folder Name:- ")

source=source+'/'
destination=destination+'/'

list_of_file=os.listdir(source)

for file in list_of_file:
    shutil.copy((source+file),destination)


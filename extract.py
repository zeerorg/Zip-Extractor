import os
from os import path
import subprocess
import zipfile

current = os.getcwd()
files = subprocess.check_output(["ls", current]).split('\n')
print files
for zipper in files[1:]:
    if zipper is not "extract.py":
        subprocess.call(["mkdir",zipper[:-4]])
        new_path = path.join(current, zipper[:-4])
        zip_path = new_path+".zip"
        print zip_path
        os.chdir(new_path)
        myzip = zipfile.ZipFile(zip_path)
        myzip.extractall()
        os.chdir(current)


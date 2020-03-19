import os
import shutil

path='Organize/'

list = os.listdir(path)

for file in list :
    file_name,extension=os.path.splitext(file)
    extension=extension[1:]
    if extension == "" :
        continue
    if os.path.exists(path+"/"+extension):
        shutil.move(path+"/"+file,path+"/"+extension+"/"+file)
    else:
        os.makedirs(path+"/"+extension)
        shutil.move(path+"/"+file,path+"/"+extension+"/"+file)
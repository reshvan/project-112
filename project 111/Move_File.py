import os
import shutil

from_dir = "C:/Users/Hai/Downloads"
to_dir = "C:/Users/Hai/Desktop"

list_of_Doc = os.listdir(from_dir)
print(list_of_Doc)

for Doc_name in list_of_Doc:
    name,extension = os.path.splitext(Doc_name)
    if extension == "":
        continue
    if extension in ['.pdf','.doc']:
        path1 = from_dir + '/' + Doc_name
        path2 = to_dir + '/' + "Doc_files"
        path3 = to_dir + '/' + "Doc_files" + '/' + Doc_name

        if os.path.exists(path2):
            print("Moving the"+Doc_name+"...")
            shutil.move(path1,path3)

        else:
            os.mkdir(path2)
            print("Moving the"+Doc_name+"...")
            shutil.move(path1,path3)
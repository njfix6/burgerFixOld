
from pathlib import Path
import os
from shutil import copyfile
from googleDrive.py import createDrivePost

pathlist = Path("/Users/nicholasfix/Pictures/").glob('**/prod/*.jpg')
i = 1
for path in pathlist:
    # because path is object not string

    src = str(path)
    placeName = src.split("/prod/")[0].split("/")[-1]
    # dst = str("/Users/nicholasfix/dev/burgerFix/themes/burgerFixTheme/source/img/"+placeName+"/post"+str(i)+"/")
    dst = str("/Users/nicholasfix/dev/burgerFix/themes/burgerFixTheme/source/img/"+placeName+"/")
    if not os.path.exists(dst):
        os.makedirs(dst)
    picture = dst+"image"+str(i)+".jpg"
    copyfile(src, picture)
    # post = open(dst+"post.txt","w")
    # post.close()

    createDrivePost(picture)

    i+=1

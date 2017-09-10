from __future__ import print_function
import os
import sys
import time
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from os import walk
from apiclient.http import MediaFileUpload
from os import listdir
from os.path import isfile, join
import re
try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None
os.chdir(sys.path[0])
from os.path import expanduser



def getDrive():
    SCOPES = 'https://www.googleapis.com/auth/drive.file'
    store = file.Storage('storage.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store, flags) \
                if flags else tools.run(flow, store)
    DRIVE = build('drive', 'v3', http=creds.authorize(Http()))
    return DRIVE

def addFile(pictureName, picturePath, driveBaseDirID):
    DRIVE = getDrive()

    file_metadata = {
      'name' : pictureName,
      'parents': [ driveBaseDirID ]
    }
    media = MediaFileUpload(picturePath,
                            mimetype='image/jpeg',
                            resumable=True)
    file = DRIVE.files().create(body=file_metadata,
                                media_body=media,
                                fields='id').execute()

def mkdir(directoryName):
    DRIVE = getDrive()

    folder_id = '0B_gjMqFEvldDMmVwOExHTkVBbG8'

    file_metadata = {
      'name' : directoryName,
      'mimeType' : 'application/vnd.google-apps.folder',
      'parents' : [folder_id]
    }

    print("test: "+ filed)
    file = DRIVE.files().create(body=file_metadata,
                                fields='id').execute()
    print ('Folder ID: ' + file.get('id'))
    return file.get('id')




def cameraToComputer():
    pass

def prodToDrive(srcPath, folderName):
    folderID = mkdir(folderName)
    pictures = expanduser(srcPath)

    print("pictrepath : "+pictures)
    imageNumber=0
    for curFile in listdir(pictures):
        curPath = join(pictures+curFile)
        if isfile(curPath) and re.match(r'.*\.JPG', curFile, re.IGNORECASE):
            print("UPLOADING FILE : "+curPath)
            addFile("image"+str(imageNumber)+".JPG", curPath, folderID)
            imageNumber+=1



def transfer():


    # transfer from camera


    prodToDrive()








def main(argv):
    # mkdir("burgerfixPosts")
    prodToDrive("/Users/nicholasfix/Pictures/camera/8:3:2017/prod/", "8/3/2017")
# time.strftime("%m/%d/%Y")
if __name__ == "__main__":
    main(sys.argv)

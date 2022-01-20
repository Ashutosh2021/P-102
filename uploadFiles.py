import time,os,shutil,dropbox
from typing import final

days=int(input("Enter the number of days file should be older than: "))
path = input("Enter the path : ")+"/"
statTime=time.time()
seconds = statTime-days*24*60*60
accessToken = "OnYZ1R0HB5UAAAAAAAAAAQ8S1Q3dTRmkdnxvCajMO_qOWA_CzC41K5_-gKmy80xX"

path_exists=os.path.exists(path)

def upload_files(file_from , file_to) :
        dbx = dropbox.Dropbox(accessToken)

        for root,dirs,files in os.walk(file_from) :
            for filename in files :
                local_path = os.path.join(root,filename)
                relative_path = os.path.relpath(local_path,file_from)
                dropbox_path = os.path.join(file_to,relative_path)

        with open(local_path,"rb") as f:
            dbx.files_upload(f.read(),dropbox_path, mode = WriteMode("overwrite"))
        print("Upload Successful !!")

if path_exists :
    uploadedFolders = 0
    uploadedFiles = 0
    fileTo = "/"+input("Enter the full path to upload to along with the file name : ")
    

    for (root,dirs,files) in os.walk(path):
        if seconds>=os.stat(root).st_ctime :
            uploadedFolders+=1
            upload_files(path,fileTo)
            break
        else :
            for folder in dirs :
                folderPath=os.path.join(root,folder)
                dropboxFolderPath = os.path.join(fileTo+folder)
                if seconds>= os.stat(folderPath).st_ctime :
                    uploadedFolders+=1
                    upload_files(folderPath,dropboxFolderPath)
                    
            for file in files :
                filePath=os.path.join(root,file)
                dropboxFilePath = os.path.join(fileTo+file)
                if seconds>= os.stat(filePath).st_ctime :
                    uploadedFiles+=1
                    upload_files(filePath,dropboxFilePath)
    
    print("Total number of uploaded folders :",uploadedFolders)
    print("Total number of uploaded files :",uploadedFiles)


else : 
    print("Path doesn't exist")
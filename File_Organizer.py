import os
import shutil

download_folder='C:\\Users\Fahumitha\Desktop\Downloads'
organized_folder='C:\\Users\Fahumitha\Desktop\Organized_Files'
folders=['Images','Documents','Audios','Videos','Spreadsheets','Others']

for folder in folders:
    os.makedirs(os.path.join(organized_folder,folder),exist_ok=True)

for filename in os.listdir(download_folder):
    if os.path.isfile(os.path.join(download_folder,filename)):

        if filename.endswith(('.png','.jpg','jpge','.gif')):
            shutil.move(os.path.join(download_folder,filename),os.path.join(organized_folder,'Images',filename))

        elif filename.endswith(('.pdf','.docx','.txt')):
            shutil.move(os.path.join(download_folder,filename),os.path.join(organized_folder,'Documents',filename))

        elif filename.endswith(('.mp3','.wav')):
            shutil.move(os.path.join(download_folder,filename),os.path.join(organized_folder,'Audios',filename))

        elif filename.endswith(('.mp4','.avi')):
            shutil.move(os.path.join(download_folder,filename),os.path.join(organized_folder,'Videos',filename))

        elif filename.endswith(('.xls','.xlsx','.csv')):
            shutil.move(os.path.join(download_folder,filename),os.path.join(organized_folder,'Spreadsheets',filename))

        else:
            shutil.move(os.path.join(download_folder,filename),os.path.join(organized_folder,'Others',filename))
            
print("File Organized successfully!")


import os
import shutil
import datetime
import schedule
import time

source_dir = "Enter your source directory's pathway here."
destination_dir = "Enter your destination directory's pathway here."

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))

    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder(s) copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder(s) already exists in: {dest}")

# schedule.every().week.at("12:00").do(lambda: copy_folder_to_directory(source_dir, destination_dir))
        
# while True:
    # schedule.run_pending()
    # time.sleep(60)

copy_folder_to_directory(source_dir, destination_dir)
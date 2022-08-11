import os, shutil, reverse, notification, sys, re

from tkinter import filedialog
from tkinter import *

# Walk through all files in the directory that contains the files to copy

def rename_and_move(source, dest):
    global show, season
    show = input('\nEnter Show name with year: ')
    season = input('Season: ')

    for root, dirs, files in os.walk(source):

        for filename in files:

            if filename == '2_English.srt':
                base = os.path.join(os.path.abspath(root))
                #Get current name
                old_name = os.path.join(base, filename)
                #Get parent folder
                parent_folder = os.path.basename(base)
                #Get episode name from folder
                episode = re.findall(r"(S\d{2}E\d{2})", parent_folder)
                new_file_name = show + ' ' + episode[0] + ".en.srt" #assuming same extension
                # print(new_file_name)
                new_abs_name = os.path.join(base, new_file_name) 
                # #Rename to new name
                os.rename(old_name,new_abs_name)
                # #Copy to destination
                dest_name = os.path.join(dest, new_file_name)
                shutil.copy(new_abs_name,dest_name)

root = Tk()
root.withdraw()

source = filedialog.askdirectory(title="Select Subtitle Folder")
dest = filedialog.askdirectory(title="Select Destination Folder")

try:
    rename_and_move(source, dest)
    reverse.reversal(source, show)
    
    if '&' in show:
        notification.send(f"*{notification.title}*\n{notification.message}\n*Season {season}* of *{show.replace('&', '%26')}*")
    else:
        notification.send(f"*{notification.title}*\n{notification.message}\n*Season {season}* of *{show}*")
except:
    print('An error occurred. Exiting...')
    sys.exit()
# Subgb v3.0
# Source Code
# Developer: moiSentineL (www.github.com/moiSentineL)
# Website: https://github.com/moiSentineL/subgb


import os, shutil, reverse, notification, sys, re

from tkinter import filedialog
from tkinter import *

# Walk through all files in the directory that contains the files to copy

def rename_and_move(source, dest):
    global show, season
    show = showentry.get()
    season = seasonentry.get()

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

def find_source():
    global source
    source = filedialog.askdirectory(title="Select Subtitle Folder")

def find_dest():
    global dest
    dest = filedialog.askdirectory(title="Select Destination Folder")

def proceed():
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

root = Tk()

# Labels
    # Show Label
l1 = Label(root, text = "Show:", font=("Arial",12,'bold')) 
l1.grid(row = 1, column = 1, sticky = W, pady= 15, padx = 5)
    # Show Entry
showentry = Entry(root, width= 30, bd=3)
showentry.grid(row = 1, column = 2, pady = 2,columnspan=2, sticky=E)
showentry.focus()
    # Season label
l2 = Label(root, text = "Season:", font=("Arial",12,'bold')) 
l2.grid(row = 2, column = 1, sticky = W,  padx = 5)
    # Season Entry
seasonentry = Entry(root, width= 5, bd=3) 
seasonentry.grid(row = 2, column = 2, sticky=W)

# Buttons
    # Button to open log file.
sourcebut = Button(root, text= "Source", command=find_source, width= 8)
sourcebut.grid(row= 2, column=3, sticky= E, padx= 5)

    # Button to delete log file.
destbut = Button(root, text= "Destination",  command=find_dest, width= 10)
destbut.grid(row= 2, column= 4, sticky= E, padx= 5)

    # Button to proceed
proceedbut = Button(root, text= "Proceed",  command=proceed, width= 8)
proceedbut.grid(row = 1, column = 4, sticky = E, padx= 5)

# Tkinter settings
window_height = 100
window_width = 440
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2.5) - (window_height/2))
# (RECOMMENDED TO NOT TOUCH) Window Metadeta.
root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
root.title('Subgb')
root.resizable(False, False)
# root.iconbitmap('thoughtlogger.ico')
root.tk.call('tk', 'scaling', 2.0)

root.mainloop()
root.withdraw()


# End of the code
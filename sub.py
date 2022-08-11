import os, shutil, reverse, notification


source = input('Source Folder: ')
dest = input('Destination Folder: ')
# Walk through all files in the directory that contains the files to copy

show = input('\nEnter Show name with year: ')
season = input('Season: ')
splitter = input('Select index position: ')

for root, dirs, files in os.walk(source):

    for filename in files:

        if filename == '2_English.srt':
            base = os.path.join(os.path.abspath(root))
            #Get current name
            old_name = os.path.join(base, filename)
            #Get parent folder
            parent_folder = os.path.basename(base)
            #Get episode name from folder
            episode = parent_folder.split(".")[int(splitter)]
            new_file_name = show + ' ' + episode + ".en.srt" #assuming same extension
            # print(new_file_name)
            new_abs_name = os.path.join(base, new_file_name) 
            # #Rename to new name
            os.rename(old_name,new_abs_name)
            # #Copy to destination
            # # one_level_up = os.path.normpath(os.path.join(base, os.pardir))
            dest_name = os.path.join(dest, new_file_name)
            shutil.copy(new_abs_name,dest_name)

reverse.reversal(source, show, splitter)
# notification.send(f'*Moanarr*\nFinished setting up subtitles for {show}; Season: {season}')

def reversal(source, show, splitter):
    import os, shutil

    # Walk through all files in the directory that contains the files to copy
    for root, dirs, files in os.walk(source):

        for filename in files:
            base = os.path.join(os.path.abspath(root))
            #Get current name
            old_name = os.path.join(base, filename)
            #Get parent folder
            parent_folder = os.path.basename(base)
            #New name based on parent folder
            episode = parent_folder.split(".")[int(splitter)]
            new_file_name = show + ' ' + episode + ".en.srt" #assuming same extension

            if filename == new_file_name:
                # print(new_file_name)
                new_abs_name = os.path.join(base, '2_English.srt') 
                # # #Rename to new name
                os.rename(old_name,new_abs_name)
                # # #Copy to one level up
                # one_level_up = os.path.normpath(os.path.join(base, os.pardir))
                # one_level_up_name = os.path.join(one_level_up, new_file_name)
                # shutil.copy(new_abs_name,one_level_up_name)
                # print(filename)

# reversal('D:\Media\Videos\Movies and TV Shows\Radarr and Sonarr\Sonarr\You.S01.1080p.WEBRip.x265-RARBG\Subs', 'You (2018)', '1')

def reversal(source, show):
    import os, shutil, re

    # Walk through all files in the directory that contains the files to copy
    for root, dirs, files in os.walk(source):

        for filename in files:
            base = os.path.join(os.path.abspath(root))
            # Get current name
            old_name = os.path.join(base, filename)
            # Get parent folder
            parent_folder = os.path.basename(base)
            # New name based on parent folder
            episode = re.findall(r"(S\d{2}E\d{2})", parent_folder)
            new_file_name = show + ' ' + episode[0] + ".en.srt" #assuming same extension

            if filename == new_file_name:
                # print(new_file_name)
                new_abs_name = os.path.join(base, '2_English.srt') 
                # Rename to new name
                os.rename(old_name,new_abs_name)


# reversal('D:\Media\Videos\Movies and TV Shows\Subtitle Extractor\Subs', 'You (2018)')
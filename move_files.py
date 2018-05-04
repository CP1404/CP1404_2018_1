"""Rename and move files from within named directories to unique files in a common directory."""
import os
import shutil

DESTINATION = 'sorted_data'

os.chdir('data')
try:
    os.mkdir(DESTINATION)
except FileExistsError:
    pass

for directory_name, directories, filenames in os.walk('.'):
    # print(directory_name, directories, files)
    if directory_name.startswith('./directory'):
        os.chdir(directory_name)
        # print(os.getcwd())
        for filename in filenames:
            number = directory_name[-1]
            parts = filename.split('.')
            new_name = "{}{}.{}".format(parts[0], number, parts[1])
            print(new_name)
            # os.rename(filename, new_name)
            shutil.move(filename, "../{}/{}".format(DESTINATION, new_name))
        os.chdir('..')

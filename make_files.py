"""Create files of various extensions in numbered folders."""

import os

EXTENSIONS = ['doc', 'xls', 'jpeg']
os.chdir('data')
for i in range(6):
    try:
        directory_name = "directory_{}".format(i)
        os.mkdir(directory_name)
    except FileExistsError:
        pass
    os.chdir(directory_name)
    # print(os.getcwd())
    for extension in EXTENSIONS:
        # touch is an OS command that creates or updates a file
        os.system("touch {}{}.{}".format("demo", "", extension))
    os.chdir('..')

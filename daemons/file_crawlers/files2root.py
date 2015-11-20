import os
import shutil
__author__ = 'Ehsan'

root = '.'
info = os.walk(root)
dir_list = []
for dir, dirs, files in info:
    dir_list = dirs
    break

for dir in dir_list:
    cu_dir = root+ '/' +dir
    info = os.walk(cu_dir)
    for r, directories, files_list in info:
        for f in files_list:
            shutil.move(r + '/' + f, './'+f)

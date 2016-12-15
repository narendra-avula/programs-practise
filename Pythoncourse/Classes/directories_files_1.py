__author__ = 'narendra'

import os

pathfiles = []

def get_dirlist(path):
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist

def print_files(path, prefix=""):
    if prefix == "":
        print "Folder listing for ", path
        prefix = "| "
    dirlist = get_dirlist(path)
    files_list = []
    for file in dirlist:
        print prefix + file
        fullpath = os.path.join(path, file)
        files_list.append(fullpath)
        if os.path.isdir(fullpath):
            print_files(fullpath, prefix + "| ")

    pathfiles.extend(files_list)

def main():
    path = "/home/narendra/iPhone/"
    print_files(path, prefix = "")
    print pathfiles

if __name__ == '__main__':
    main()
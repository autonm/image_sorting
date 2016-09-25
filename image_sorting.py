import cmd
import os
import platform
import sys
import time
import datetime
import shutil
import exif
from PIL import Image

def walk_folders(walk_this):
    # walk_dir = sys.argv[1]
    walk_dir = walk_this

    print('walk_dir = ' + walk_dir)

    # If your current working directory may change during script execution, it's recommended to
    # immediately convert program arguments to an absolute path. Then the variable root below will
    # be an absolute path as well. Example:
    # walk_dir = os.path.abspath(walk_dir)
    print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))

    for root, subdirs, files in os.walk(walk_dir):
        print('--\nroot = ' + root)
        list_file_path = os.path.join(root, 'my-directory-list.txt')

        with open(list_file_path, 'wb') as list_file:
            for subdir in subdirs:
                print('\t- subdirectory ' + subdir)

            for filename in files:
                if filename.endswith(".jpg"):
                    file_path = os.path.join(root, filename)
                    created_date = time.strftime('%m %Y', time.gmtime(os.path.getmtime(file_path)))
                    print('\t- file %s (full path: %s, created date: %s)' % (filename, file_path, created_date))

                    newpath = r'C:\Users\Michael\Desktop\new gallery'
                    if not os.path.exists(newpath):
                        os.makedirs(newpath)

                    print newpath
                    print filename
                    move_to = ''.join([newpath, "\\", filename])
                    print "move from: %s" % file_path
                    print "move to: %s" % move_to
                    shutil.copy2(file_path, move_to)

# srcfile = 'a/long/long/path/to/file.py'
# dstroot = '/home/myhome/new_folder'

# assert not os.path.isabs(srcfile)
# dstdir =  os.path.join(dstroot, os.path.dirname(srcfile))

# os.makedirs(dstdir) # create all directories, raise an error if it already exists
# shutil.copy(srcfile, dstdir)


def creation_date(path_to_file):
    """
    Try to get the date that a file was created, falling back to when it was
    last modified if that isn't possible.
    See http://stackoverflow.com/a/39501288/1709587 for explanation.
    """
    if platform.system() == 'Windows':
        return os.path.getctime(path_to_file)
    else:
        stat = os.stat(path_to_file)
        try:
            return stat.st_birthtime
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            return stat.st_mtime


def main():
    print "Folder/Image Organisation"
    print ""
    walk_folders("C:\Users\Michael\Desktop\phone")

if __name__ == "__main__":
    main()




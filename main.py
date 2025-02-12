# Get the currently directory

import os


# cwd = os.getcwd()
# print(cwd)

# Change the current working directory

# os.chdir('/main2')
# swd = os.getcwd()
# print(swd)

# Join and split a path

# fp = os.path.join('temp', 'python')
# print(fp)  # temp\python (on Windows)

# pc = os.path.split(fp)
# print(pc)  # ('temp', 'python')

# Test if a path is a directory

# dir = os.path.join("C:\\", "temp")
# print(dir)

# if os.path.exists(dir) or os.path.isdir(dir):
#     print(f'The {dir} is a directory')

# Create a directory

# dir = os.path.join("C:\\", "temp", "python")
# if not os.path.exists(dir):
#     os.mkdir(dir)

# Rename a directory

# oldpath = os.path.join("C:\\", "temp", "python")
# newpath = os.path.join("C:\\", "temp", "python3")

# if os.path.exists(oldpath) and not os.path.exists(newpath):
#     os.rename(oldpath, newpath)
#     print("'{0}' was renamed to '{1}'".format(oldpath, newpath))

# Delete a directory


# dir = os.path.join("C:\\","temp","python")
# if os.path.exists(dir):
#     os.rmdir(dir)
#     print(dir + ' is removed.')

# Traverse a directory recursively

# path = "c:\\temp"
# for root, dirs, files in os.walk(path):
#     print("{0} has {1} files".format(root, len(files)))

# Summary

    # Use the os.getcwd() function to get the current working directory.
    # Use the os.chdir() function to change the current working directory to a new one.
    # Use the os.mkdir() function to make a new directory.
    # Use the os.rename() function to rename a directory.
    # Use the os.rmdir() function to remove a directory.
    # Use the os.walk() function to list the contents of a directory.
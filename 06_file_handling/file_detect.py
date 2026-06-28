#Python file detection
import os

file_path="fileHandling/test.txt"

if os.path.exists(file_path):
    print("File exists")
    if os.path.isfile(file_path):
        print("File is a regular file")
    elif os.path.isdir(file_path):
        print("File is a directory")
    else:
        print("File is not a regular file")
else:
    print("File does not exist")
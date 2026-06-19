import os

# Specify the directory path
path = "new folder"

# Get and print all files and folders in the directory
contents = os.listdir(path)

for item in contents:
    print(item)
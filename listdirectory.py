# Print the contents of the directory using os module in Python.

import os 

# Specify the directory path
directory_path = "/PythonProjects"

# List all files and directories in the specified path  
contents = os.listdir(directory_path)

# Print the contents
for item in contents:
    print(item)

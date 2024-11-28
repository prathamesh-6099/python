# Q. Write a python program to print the contents of a directory using the os module.
#Search online for the function which does that.
# Label the program written in problem 4 with comments

import os  # Import the os module

# Specify the directory you want to list
directory = '/'  # Replace this with the path to the directory you want to list

# Get a list of all files and directories in the specified directory
contents = os.listdir(directory)  # os.listdir() returns a list of all files and directories in the given directory

# Print the contents of the directory
print(contents)
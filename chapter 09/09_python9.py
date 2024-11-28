# Write a program to find out whether a file is identical & matches the content of 
# another file.

with open("chapter 09\problem9_file1.txt") as f:
    content1= f.read()
with open("chapter 09\problem9_file2.txt") as f:
    content2=f.read()
if(content1==content2):
    print("Two file is idendical!")
else:
    print("Two file is not idendical!")
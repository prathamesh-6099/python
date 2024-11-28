#  A file contains a word “Donkey” multiple times. You need to write a program 
# which replace this word with ##### by updating the same file. 

with open("chapter 09\problem4_file.txt", "r") as f:
    content=f.read()
    

with open("chapter 09\problem4_file.txt", "w") as f:
    newcontent=content.replace("donkey", "####")
    f.write(newcontent)
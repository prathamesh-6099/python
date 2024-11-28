# Write a program to make a copy of a text file “this. txt”

with open("chapter 09/this.txt") as f:
    content=f.read()
with open("chapter 09/this_copied.txt", "w") as f:
    f.write(content)
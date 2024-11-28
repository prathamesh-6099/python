#Write a python program to rename a file to “renamed_by_ python.txt
with open("chapter 09\old.txt") as f:
    content=f.read()
with open("chapter 09\Renamed_old.txt", "w") as f:
    f.write(content)

# Repeat program 4 for a list of such words to be censored.

words=["donkey", "bad", "black"]
with open("chapter 09\problem4_file.txt", "r") as f:
    content=f.read()
    

with open("chapter 09\problem4_file.txt", "w") as f:
    for word in words:
      content=content.replace(word, "####")
    f.write(content)
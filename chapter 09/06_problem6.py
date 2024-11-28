#Write a program to mine a log file and find out whether it contains ‘python’

with open("chapter 09\log_prob6.txt","r") as f:
    content=f.read()
    if("python" in content):
        print("python word is present in this file")
    else:
        print("python word is not present in this file")
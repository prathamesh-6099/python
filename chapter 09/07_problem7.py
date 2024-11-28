# Write a program to find out the line number where python is present from ques 6.
with open("chapter 09\log_prob6.txt","r") as f:
    lines=f.readlines()

lineno=1 
   
for line in lines:
    if("python" in line):
        print(f"python word is present in this file in line {lineno}")
        break
    lineno+=1
else:
    print("python word is not present in this file")
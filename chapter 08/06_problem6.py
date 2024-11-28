#Write a python function which converts inches to cms.

def convert(n):
    return n*2.54
num=int(input("Enter Number: "))
print(convert(num),"cms")
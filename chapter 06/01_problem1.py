# . Write a program to find the greatest of four numbers entered by the user
n1=int(input("Enter number 1: "))
n2=int(input("Enter number 2: "))
n3=int(input("Enter number 3: "))
n4=int(input("Enter number 4: "))

if(n1>n2 and n1>n3 and n1>n4):
    print(n1,"is greater")  

elif(n2>n1 and n2>n3 and n2>n4):
    print(n2, "is greater")
elif(n3>n1 and n3>n2 and n3>n4):
    print(n3, "is greater")
else:
    print(n4, "is greater") 



#. Write a program to find whether a given number is prime or not
number=int(input("Enter  Number: "))
value=False
for i in range(2,number):
    if(number%i==0):
        value=True
        #  print(f"{number} is Prime")
        break
    else:
        i=i+1   
# else:
#        print(f"{number} is not Prime") ....THIS is also true
if(value==False):
    print(f"{number} is Prime")
else:
    print(f"{number} is not Prime")

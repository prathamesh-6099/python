# . Write a program to print the following star pattern.
#  *
# ***
#***** for n = 3
# end=" " <<< this continue line without break
n=int(input("Enter number: "))
for i in range(1,n+1):
    print(" "*(n-i), end="")
    print("*"*((2*i)-1))
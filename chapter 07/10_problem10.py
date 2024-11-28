# . Write a program to print multiplication table of n using for loops in reversed 
# order.
n=int(input("Enter number: "))
i=10
for i in range(1,11):
    print(f"{n}× {11-i}={n*(11-i)}")

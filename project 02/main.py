# We are going to write a program that generates a random number and asks the user to 
# guess it.
# If the player’s guess is higher than the actual number, the program displays “Lower 
# number please”. Similarly, if the user’s guess is too low, the program prints “higher 
# number please” When the user guesses the correct number, the program displays the 
# number of guesses the player used to arrive at the number.
# Hint: Use the random module

from random import randint

n=int(randint(1,100))
guesses=1
a=-1
while(a!=n):
    a=int(input("Guess the number"))
    if(n>a):
        print("Enter greater number please..")
        guesses+=1
    elif(n<a):
         print("Enter smaller number please..")
         guesses+=1
print(f"finally you have gussed the number {n} in {guesses} attempt..")

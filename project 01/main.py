'''

PROJECT 1: SNAKE, WATER, GUN GAME
We all have played snake, water gun game in our childhood. If you haven’t, google the 
rules of this game and write a python program capable of playing this game with the 
user

Snake:-1
Water: 0
GUN:1

Summary!!!
Snake beats Water.
Water beats Gun.
Gun beats Snake.

!!!
please Enter s: for snake , w:for water, g: for gun
!!!

'''
import random
computer=random.choice([-1,0,1])
you=input("Enter Your choise: ").lower()
dic={"s":-1,"w":0, "g":1}
reverse_dic={-1:"snake", 0:"water", 1:"gun"}
yourchoise=dic[you]
print(f"your choise is: {reverse_dic[yourchoise]} and computer choise: {reverse_dic[computer]}")

if(computer==yourchoise):
    print("its a Draw!!")
else:
    if(computer==-1 and yourchoise==0):
        print("You lose!!")
    elif(computer==-1 and yourchoise==1):
        print("You Win!!")
    elif(computer==0 and yourchoise==-1):
        print("You Win!!")
    elif(computer==0 and yourchoise==1):
        print("You Lose!!")
    elif(computer==1 and yourchoise==-1):
        print("You Lose!!")
    elif(computer==1 and yourchoise==0):
        print("You Win!!")
    
    else:print("Something went wrong!!")
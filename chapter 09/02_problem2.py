# The game() function in a program lets a user play a game and returns the score 
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or 
# contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score

import random
def game():
    score=random.randint(1,50)
    print(f"your score is :{score}")
    with open("chapter 09\hiscore.txt") as f:
        hiscore=f.read()
        if(hiscore==""):
            hiscore=0
        else:
            hiscore=int(hiscore)

   
        if(score>hiscore):
             with open("chapter 09\hiscore.txt", "w") as file:
           
              file.write(str(score))    
 
game()
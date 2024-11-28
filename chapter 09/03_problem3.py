# Write a program to generate multiplication tables from 2 to 20 and write it to the 
# different files. Place these files in a folder for a 13 – year old.
import os 
def tables(n):
    table=""
    for i in range(1,11):
        table+=f"{n}×{i}={n*i}\n"
    
    with open(f"chapter 09\prob_3_tables\ table_{n}.txt","w") as f:
        f.write(table)
 


for i in range(1,21):
    tables(i)

print("Multiplication Table from 1 to 20 created succesfully !!")
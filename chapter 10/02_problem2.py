# Write a class “Calculator” capable of finding square, cube and square root of a 
# number.
class Calcualator:
     def __init__(self,num):
         self.num=num
     
     def square(self):
         square=self.num*self.num
         print("Square of number: ", square)
    
     def cube(self):
         cube=self.num**3
         print("Cube of number: ", cube)         
    
     def sqrt(self):
         sqrt=self.num**1/2
         print("Square root of number: ", sqrt)

num=int(input("Enter number to perform opperations: \n"))
n1=Calcualator(num)
n1.square()
n1.cube()
n1.sqrt()
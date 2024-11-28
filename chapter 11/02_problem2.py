# Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from 
# ‘Pets’. Add a method ‘bark’ to class ‘Dog’.

class Animals:
      def __init__(self):
           pass

class Pets(Animals):
      def __init__(self):
           pass


class Dog(Pets):
    @staticmethod
    def bark():
        print("Bow Bow !!")

D1=Dog()
D1.bark()
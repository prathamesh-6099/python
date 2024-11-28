# Create a class (2-D vector) and use it to create another class representing a 3-D
# vector.
class TwoDvector:
    def __init__(self,x,y):
        self.x=x
        self.y=y

class ThreeDvector(TwoDvector):
    
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.z=z
    def show(self):
        print(f"{self.x}i + {self.y}j + {self.z}k")


O1=TwoDvector(1,2)
o2=ThreeDvector(1,2,3)
o2.show()
        
    

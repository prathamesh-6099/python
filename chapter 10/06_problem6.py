# Can you change the self-parameter inside a class to something else (say
# “harry”). Try changing self to “slf” or “harry” and see the effects.
from random import randint 
class Train:
    def __init__(slf,id): # no there is no impact of changing name of self parameter but changed name also used in function
        slf.id=id

    def book(self, frm, to):
        print(f"your ticket {self.id} has been booked from {frm} to {to}")
    
    def status(self,frm,to):
        print(f"Your train is running from {frm} to {to} on a time under indian railways")
    
    def fare(self):
        print(f"your ticket prize is {randint(1000,2000)}")
    



person1=Train(123456)
person1.book("pune", "goa")
person1.status("pune", "Goa")
person1.fare()
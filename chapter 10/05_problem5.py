#  Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
# and get fare information of train running under Indian Railways
from random import randint 
class Train:
    def __init__(self,id):
        self.id=id

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
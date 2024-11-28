#Write a python program using function to convert Celsius to Fahrenheit.
#°F = °C × (9/5) + 32.

def convirsion(val):
    F=val*(9/5)+32
    return F

cel=int(input("Enter Temprature: "))
c=convirsion(cel)
print(round(c,2),"°F")

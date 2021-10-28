"""
a= input("Enter anme of user")
b= input("enter number")
if b==0:
    raise  ZeroDivisionError("You eneter 0")
if a.isnumeric():
    raise Exception("numbers not allowed")"""

a= input("eneter")
try:
    print(b)
except Exception as e:
    if a=="gar":
         raise ValueError("he is don")
    print("Exception handel")

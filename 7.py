#asking user to give a number
number=input("give a number:")
#converting number to integer form
number=int(number)
#checking whther number is positive,negative,or zero
if number>0:
    print("The number given by the user is positive")
elif number<0:
    print("The number given by the user is negative")
else:
    print("The number given by the user is zero")


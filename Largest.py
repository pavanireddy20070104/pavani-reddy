#Write a program to find the largest of three numbers.
num1=int(input("ENTER THE NUM1:"))
num2=int(input("ENTER THE NUM2:"))
num3=int(input("ENTER THE NUM3:"))
if num1 >= num2 and num1 >= num3:
    print(num1)
elif num2 >= num1 and num2 >= num3:
    print(num2)
else:
    print(num3)

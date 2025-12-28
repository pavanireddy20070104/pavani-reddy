#asking user for two numbers in the form of strings
num1=input("enter num1 value:")
num2=input("enter num2 value:")
#converting numbers in the form of strings to integers
num1=int(num1)
num2=int(num2)
#performing arithmetic operations like sum,difference,product
sum=num1+num2
difference=num1-num2
product=num1*num2
#displaying outputs for arithmetic operators
print("sum of two numbers num1 and num2:",sum)
print("difference of two numbers num1 and num2:",difference)
print("product of two numbers num1 and num2:",product)
#checking whether which one is bigger or equal to
if num1>num2:
    print("The maximum of two numbers is",num1)
elif num1<num2:
    print("The maximum of two numbers is",num2)
else:
    print("Both the numbers are equal")
    

#CRETAING AGE VARIABLE
age=input("enter your age:")
#coverting age string to integer
age=int(age)
#PRINTING DIFFERENT MESSAGES FOR DIFFERENT AGES
if age<13:
    print("You are child")
elif 13 <= age <= 17:
    print("You are a teenager")
elif 18 <= age <= 64:
    print("You are an adult")
else:
    print("You are a senior")


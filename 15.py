#creating an  list
number_list = [12, 45, 3, 98, 7, 34, 21]
#printing numbers in number_list
for num in number_list:
    print("The numbers in the number_list are:",num)
#printing numbers in the list greater than 30
number = 30
for numbers in number_list:
    if numbers>number:
        print("numbers in the list greater than 30 are:",numbers)
#counting numbers in the list that are greater than 30 
number = 30
count=0
for numbers in number_list:
    if numbers>number:
        count += 1
        print("Count of numbers greater than 30 is", count)

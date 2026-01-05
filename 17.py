import random
# Create a list of 8 random integers between 1 and 100
numbers = []
for i in range(8):
    numbers.append(random.randint(1, 100))
print("List:", numbers)
largest = numbers[0]
smallest = numbers[0]
# Find largest and smallest using loop
for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
print("Biggest number:", largest)
print("Smallest number:", smallest)

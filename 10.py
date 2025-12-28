#ask user for temparature in celsius
c=int(input("give the temperature in celsius:"))
#converting celsius to fahrenheit
f=(c*9/5)+32
print("The temparuture in fahrenheit",f)
#giving advice according to celsius temperature
if c <0:
    print("Very cold! Wear thick jacket")
elif 0 <= c <= 15:
    print("Cold. Wear jacket")
elif 16 <= c <= 25:
    print("Nice weather")
else:
    print("Hot! Stay hydrated")

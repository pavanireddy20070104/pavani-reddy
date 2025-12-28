#finding secret number
secret_number=7
guess_number=int(input("enter your guess number:"))
while guess_number != secret_number:
    if guess_number > secret_number:
        print("Too high")
    else:
        print("Too low")

    guess_number= int(input("guess again:"))
print("You guessed the correct number")


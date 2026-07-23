import random
secret_number = random.randint(1, 100)

guess = int(input("guess the number: "))
while guess != secret_number:

    if guess > secret_number:
        print("too high")
    elif guess < secret_number:
        print("too low")

    guess = int(input("Try again: "))

print("you guessed correctly!")


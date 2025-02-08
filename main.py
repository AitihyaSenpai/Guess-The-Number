import random

random_number = int(random.randint(1, 100))

guess = 1
initial_score = 110
print(
    "Game rules:\n 1. You got 10 guess \n 2. Initial score is 100 \n 3. For every guess you lose 10 points(first guess doesn't count). \n Now lets start!"
)
while True:
    try:
        guessed_number = int(input("Guess the number: "))

    except ValueError:
        print("Enter a valid number bro!")
        continue

    if guessed_number > 100:
        print("Bro wake up to reality\n")

    elif guessed_number <= 0:
        print("You got a big brain BRUV!")

    elif guessed_number < random_number:
        print("The number is a bit bigger!\n")

    elif guessed_number > random_number:
        print("The number is a bit smaller!\n")

    if guessed_number == random_number:
        print("Hurray you won!😃")
        break
    guess += 1
    if guess == 11:
        print("you lose! 😿")
        break
score = initial_score - guess * 10


print(f"The number was {random_number} !")
print(f"Your score was : {score} 🫂")

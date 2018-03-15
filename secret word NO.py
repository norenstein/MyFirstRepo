import random

number = random.randint(0,3)

words = ["lucky landing","tilted towers", "flush factory", "pleasant park"]
hint1 = ["new spot","overpopulated", "old place", "zoo"]
hint2 = ["fortnite","fortnite","fortnite","fortnite"]

secretword = words[number]

guess= ""
counter = 1

while True:
    print("Guess the secret word")
    print("Type 'hint1', 'hint2', 'first letter', or 'give up' for answer.")
    guess = input()

    if guess == secretword:
        print("You win!")
        print("It took you " + str(counter) + " guesses.")
        break
    elif guess == "hint1":
        print(hint1[number])
    elif guess == "hint2":
        print(hint2[number])
    elif guess == "first letter":
        print(secretword[0])
    elif guess == "give up":
        print("Wow. You gave up.")
        print("You failed " + str(counter)+ " times.")
        break

    else:
        print("Guess again.")
        coounter += 1

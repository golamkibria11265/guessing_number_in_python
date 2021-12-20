import random

print("""Welcome to the number guessing game
I am thinking of a number between 1 and 100.""")

game_type = input("Choose a difficulty. Type easy or hard:\n")

guessing_num = random.randint(1, 100)


def game_level():
    if game_type == "easy":
        return 10
    elif game_type == "hard":
        return 5


attempt = game_level()


def check_the_num(parameter):
    guessed_num = int(input("Make a guess:"))
    if guessed_num > parameter:
        print("The number is too High")
    elif guessed_num < parameter:
        print("The number is too Low")
    elif guessed_num == parameter:
        print("You got the number")


for i in range(attempt):
    check_the_num(guessing_num)

import random


def game_on(a):
    for i in range(a):
        print(f"You have {a - i} attempts remaining to guess the number")
        user_attempt = int(input("Make a guess: "))
        if user_attempt > computer_number:
            print("Too high")
        elif user_attempt < computer_number:
            print(" Too low")
        else:
            print(f"You are correct. The number was {computer_number}")
            break


computer_number = random.randint(1, 100)
print(f"Welcome to the Number Guessing Game! \n"
      f"I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ")

match level:
    case "easy":
        easy_attempts = 10
        game_on(easy_attempts)

    case "hard":
        attempts = 5
        game_on(attempts)

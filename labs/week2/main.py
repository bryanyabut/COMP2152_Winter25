import random


def number_gussing_game():
    targetNumber = random.randint(1, 100)

    play = input("Do you want to play number guessing game? (yes/no)").strip().lower()

    attemps = 0
    max_attemps = 10

    while attemps < max_attemps:
        try:
            userGuess = int(input("Enter your guess: "))
            # attempts = attempts + 1
            attemps += 1
            if userGuess < targetNumber:
                if abs(userGuess - targetNumber) <= 5:
                    print("Too low! You're very close! Try again.")
                else:
                    print("Too low, try again.")
            elif userGuess > targetNumber:
                if abs(userGuess - targetNumber) <= 5:
                    print("Too High! You're very close! Try again.")
                else:
                    print("Too high! Try again.")
            else:
                print(f"Congratulation! You've guessed it in {attemps} attempts.")
                return
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 100")
    print(f"Game over! The target number was {targetNumber}.")


number_gussing_game()

# targetNumber = random.randint(1,100)
# userGuess = 0
#
# print (targetNumber)
# minPossible = 0
# maxPossible = 100
#
# while userGuess != targetNumber:
#     userGuess = int(input("Guess a number between 1 and 100: "))
#     if userGuess > targetNumber:
#         print("Too high! Try again.")
#         if userGuess < minPossible:
#             minPossible = userGuess - 1
#     elif userGuess < targetNumber:
#         print("Too low! Try again.")
#         if userGuess > maxPossible:
#             maxPossible = userGuess - 1
#     else:
#         print("Game Over! The number was " + targetNumber, "The Player wins!")
#         break

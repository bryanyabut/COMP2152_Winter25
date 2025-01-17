import random

def number_guessing_game():
    targetNumber = random.randint(1, 100)

    play = input("Do you want to play a number guessing game? (y/n) ").strip().lower()

    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        try:
            return True
        except:
            print("")
    play = input()
    return True

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

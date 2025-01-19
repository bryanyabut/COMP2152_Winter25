import random

weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]

try:
    weaponRoll = random.randint(1, 6)

    combatStrength = 0
    combatStrength += weaponRoll

    chosenWeapon = weapons[weaponRoll - 1]

    print(f"Your weapon: {chosenWeapon}")

    if weaponRoll <= 2:
        print("You rolled a weak weapon, friend.")
    elif weaponRoll <= 4:
        print("Your weapon is meh.")
    else:
        print("Nice weapon, friend!")

    if chosenWeapon != "Fist":
        print("Thank goodness you didn't roll the Fist...")

except ValueError:
    print("HALT!! Invalid input! Please enter a valid number.")
except Exception as e:
    print(f"An error occurred: {e}")
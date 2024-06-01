import random
import sys

def diceroll(dice, sides):
    roll = 0
    for i in range(dice):
        roll += random.randint(1, sides)
    # Give special output if all dice roll max or min values
    if roll == dice:
        return f"Critical failure! {roll}"
    elif roll == dice * sides:
        return f"Critical success! {roll}"
    else:
        return f"You rolled: {roll}"

if len(sys.argv) != 3:
    print("Usage: python script.py [number of dice] [number of sides]")
    sys.exit(1)

try:
    d = int(sys.argv[1])
    if d == 0:
        print("You can't roll without dice..")
        sys.exit(1)
except ValueError:
    print("Invalid number of dice.")
    sys.exit(1)

try:
    s = int(sys.argv[2])
    if s < 2:
        print("That's not a dice....")
        sys.exit(1)
except ValueError:
    print("Invalid number of sides.")
    sys.exit(1)

result = diceroll(d, s)
print(result)

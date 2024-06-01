import random
import argparse

def argparse_helper():
    parser = argparse.ArgumentParser(description="Roll a dice")
    parser.add_argument("dice", type=int, action="store",default=False, help="Number of dice")
    parser.add_argument("sides", type=int, action="store",default=False, help="Number of sides per dice")
    parser.add_argument("--version", action="version", version="%(prog)s 1.0")
    args = parser.parse_args()
    
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
def main():
    args = argparse_helper()
    if args.dice == 0:
        print("You can't roll without dice..")
        return

    if args.sides < 2:
        print("That's not a dice....")
        return

    result = diceroll(args.dice, args.sides)
    print(result)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

#!usr/bin/env python3

import random 

def diceroll(dice, sides):
        roll = 0
        for i in range(dice):
             roll += random.randint(1,sides)
        #Give special output if all dice roll max or min values
        if roll == dice:
             return(f"Critical failure! {roll}")
        elif roll == dice*sides:
            return(f"critical success!{roll}")
        else:
            return(f"you rolled: {roll}")

d = int(input("how many dice?:"))
if d == 0:
        print ("you can't roll without dice..")
        exit()

s = int(input("how many sides per dice?:"))
if s < 2:
        print("Thats not a dice....")
        exit()
result = diceroll(d,s)
print(result)

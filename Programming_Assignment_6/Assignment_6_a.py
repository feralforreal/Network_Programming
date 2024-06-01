#!/usr/bin/env python3

#A small code to measure the volume of the cylinder
import math

def cylindervol(radius, height):
    vol = (math.pi) * (radius ** 2) * (height)
    return (vol)

if __name__ == "__main__":
     print(cylindervol(2,4))


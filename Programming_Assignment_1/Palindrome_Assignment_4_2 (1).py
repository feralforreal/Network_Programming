#!/bin/bash/env python3

#using reversed_function() to check if a string is palindrome
print("Check the palindrome functionality using Splice-string flip method :")
normal = input("Enter the palindrome Value: ")
print(normal[::-1])
print("")
print("Check the plaindrome functionality using Reverse() method")
x = input ("Enter the palindrome value : ")
def palindrome(x):
    x = x.lower().replace(' ','')
    reverse_x = ''.join(reversed(x))
    return x == reverse_x
if (palindrome(x)) == True:
    print("yes! the input is a palindrome")
else:
    print("No! the input is not a palindrome")


'''palin = "hello" '''
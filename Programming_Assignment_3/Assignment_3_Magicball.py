#!/usr/bin/python3
import random

def magic_8_ball(fortunes, question):
    response = random.choice(fortunes)
    return f"Question: {question}\nMagic 8-Ball says: {response}"

def main():
    default_fortunes = [
        "It is certain.",
        "Without a doubt.",
        "You may rely on it.",
        "Yes, definitely.",
        "As I see it, yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Cannot predict now."
    ]
    
    print("Welcome to the Magic 8-Ball!")
    print("Default fortunes are loaded.")
    
    num_fortunes = int(input("How many additional fortunes do you want to add? (Enter 0 if none): "))
    additional_fortunes = []
    for i in range(num_fortunes):
        fortune = input(f"Enter fortune {i+1}: ")
        additional_fortunes.append(fortune)
    
    fortunes = default_fortunes + additional_fortunes
    
    while True:
        user_input = input("Ask a question (type 'quit' to exit): ")
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        else:
            print(magic_8_ball(fortunes, user_input))

if __name__ == "__main__":
    main()

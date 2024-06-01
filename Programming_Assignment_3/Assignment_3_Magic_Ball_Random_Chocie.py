import random

def magic_8_ball():
    fortunes = [
        "It is certain.",
        "Without a doubt.",
        "You may rely on it.",
        "Yes, definitely.",
        "As I see it, yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Cannot predict now."
    ]
    index = random.randint(0, len(fortunes) - 1)
    return fortunes[index]

if __name__ == "__main__":
    print("Welcome to the Magic 8-Ball!")
    while True:
        user_input = input("Ask a question (type 'quit' to exit): ")
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        else:
            print("The Magic 8-Ball says:", magic_8_ball())

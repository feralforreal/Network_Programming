def main():
    word = input("Enter a word: ")
    if word.isalpha() != True:
        print("\n Input given is not a word!\n")
    elif len(word) <= int(4):
        print("Word is too short. It should have at least 4 letters.")
    else:
        fourth_letter = word[3]
        last_letter = word[-1]
        print(f"The 4th letter of '{word}' is '{fourth_letter}' and the last letter is '{last_letter}'.")

if __name__ == "__main__":
    main()

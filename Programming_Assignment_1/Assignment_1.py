import argparse

def main(fruits):
    fruits.sort()
    print("Sorted list of fruits:")
    for fruit in fruits:
        print(fruit)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sort and print a list of fruits.")
    parser.add_argument('fruits', metavar='fruit', type=str, nargs=3,
                        help='Three fruits to sort and print')
    
    args = parser.parse_args()
    main(args.fruits)

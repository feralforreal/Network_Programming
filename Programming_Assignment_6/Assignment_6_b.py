# Custom lists of keys and values
keys = ["a", "b", "c", "d"]
values = [1, 2, 3, 4]

# Create a dictionary from the lists
my_dict = dict(zip(keys, values))

# Print just the keys
print("Keys:", list(my_dict.keys()))

# Print just the values
print("Values:", list(my_dict.values()))

# Print the dictionary itself
print("Dictionary:", my_dict)

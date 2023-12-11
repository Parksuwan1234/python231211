#Chatgpt.py
# List
my_list = [1, 2, 3, 4, 5]
print("List:", my_list)

# Tuple
my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)

# Set
my_set = {1, 2, 3, 4, 5}
print("Set:", my_set)

# Dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print("Dictionary:", my_dict)

# Accessing elements
print("\nAccessing elements:")
print("List - Element at index 2:", my_list[2])
print("Tuple - Element at index 2:", my_tuple[2])
# Sets don't support indexing, so we'll convert it to a list for demonstration
set_as_list = list(my_set)
print("Set - Element at index 2:", set_as_list[2])
print("Dictionary - Value for key 'c':", my_dict['c'])

# Modifying elements
print("\nModifying elements:")
my_list[2] = 10
# Tuples are immutable, so we need to create a new tuple
my_tuple = my_tuple[:2] + (10,) + my_tuple[3:]
my_set.add(10)
my_dict['c'] = 30

# Iterating through elements
print("\nIterating through elements:")
print("List:")
for item in my_list:
    print(item)

print("Tuple:")
for item in my_tuple:
    print(item)

print("Set:")
for item in my_set:
    print(item)

print("Dictionary:")
for key, value in my_dict.items():
    print(f"{key}: {value}")
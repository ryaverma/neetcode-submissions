# Dictionaries can't contain duplicate keys, just like sets.
# The values within a dictionary can be of any type, including lists, sets, and even other dictionaries.

your_dict = { 
  "a": 10, 
  "apple": 12,
  "bat": 7
}

print(your_dict)
print(your_dict["a"])
print("d" in your_dict)
your_dict["a"] = 4
print(your_dict)
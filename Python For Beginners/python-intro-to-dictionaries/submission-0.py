# Dictionaries are used to store key-value pairs.
# Another way of phrasing it is we are mapping a key to the value. This is why dictionaries are sometimes called maps or hashmaps in other programming languages.
# To declare an empty dictionary we can use empty curly braces {}. We can then add key-value pairs to the dictionary using square brackets [] and the assignment operator =. This is similar to lists, but keys don't have to be integers.

from typing import List, Dict

def create_dict(name: str, age: int) -> Dict[str, int]:
    mydict = {}
    mydict[name] = age
    return mydict


def list_to_dict(words: List[str]) -> Dict[str, int]:
    mydict = {}
    for i in range(len(words)):
        mydict[words[i]] = i
    return mydict

# don't modify code below this line
print(create_dict("Alice", 25))
print(create_dict("Jane", 35))
print(create_dict("Joe", 45))

print(list_to_dict(["Alice", "Jane", "Joe"]))
print(list_to_dict(["Apple", "Banana", "Watermelon", "Pineapple"]))

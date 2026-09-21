# You can remove an item from a dictionary using the pop() function. This function takes a key as an argument and removes the key-value pair from the dictionary. If the key doesn't exist, it will raise a KeyError.
# If you don't want to worry about handling the KeyError, you can use the second argument of the pop() function. - value = my_dict.pop("d", 0)
# You can also use the del keyword to remove a key-value pair from a dictionary. - del my_dict["a"]

from typing import Dict, List

def remove_keys(my_dict: Dict[str, int], keys: List[str]) -> Dict[str, int]:
    for i in range(len(keys)):
        if keys[i] in my_dict:
            my_dict.pop(keys[i])
    return my_dict

# do not modify below this line
print(remove_keys({"a": 1, "b": 2, "c": 3}, ["a", "c"]))
print(remove_keys({"a": 1, "b": 2, "c": 3}, ["d"]))

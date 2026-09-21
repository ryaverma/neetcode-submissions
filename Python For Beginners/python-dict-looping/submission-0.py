# You can use len() to get the length of a dictionary. This will return the number of key-value pairs in the dictionary. But just like with sets, the length of a dict won't help us to loop over it. The good news is that looping over a dictionary is very similar to looping over a set. We can also use the items() method to loop over both the keys and values at the same time.

from typing import Dict, List # this adds type hints for List and Dict

def get_dict_keys(age_dict: Dict[str, int]) -> List[str]:
    names = []
    for key in age_dict:
        names.append(key)
    return names

def get_dict_values(age_dict: Dict[str, int]) -> List[int]:
    ages = []
    for key, value in age_dict.items():
        ages.append(value)
    return ages

# do not modify below this line
dict_1 = {"John": 25, "Doe": 30, "Jane": 22}
dict_2 = {"NeetCode": 24, "NeetCode2": 25, "NeetCode3": 26}

print(get_dict_keys(dict_1))
print(get_dict_keys(dict_2))

print(get_dict_values(dict_1))
print(get_dict_values(dict_2))

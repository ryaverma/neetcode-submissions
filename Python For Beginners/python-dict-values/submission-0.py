# This function allows us to loop over the values in the dictionary without needing to access the keys.

from typing import Dict, List

def get_dict_values(age_dict: Dict[str, int]) -> List[int]:
    age_list = []
    for values in age_dict.values():
        age_list.append(values)
    return age_list

# do not modify below this line
print(get_dict_values({"Alice": 25, "Bob": 30, "Charlie": 35}))
print(get_dict_values({"Alice": 25, "Bob": 30, "Charlie": 35, "David": 40}))

# One of the most common uses of a dictionary is to count the occurences of elements in a list. For example, given the list [1, 2, 3, 1, 2, 3, 1, 2, 3], we can count the quantity of each element in the list using a dictionary.

from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    count_dict = dict()
    for i in range(len(word)):
        char = word[i]
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    return count_dict

# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))

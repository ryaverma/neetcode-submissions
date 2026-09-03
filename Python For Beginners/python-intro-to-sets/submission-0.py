# In Python, a set is very similar to a list, but with a few key differences.
# A set is unordered, meaning the elements are not stored in a specific order. If order is important, you should use a list.
# A set can only contain unique elements. If you try to add a duplicate element to a set, it will be ignored. A set can be created using curly braces {} with elements separated by commas.

from typing import List, Set # this adds type hints for List and Set

def list_to_set(nums: List[int]) -> Set[int]:
    myset = set()
    for i in nums:
        myset.add(i)
    return myset

# do not modify below this line
print(list_to_set([1, 2, 3, 4, 5]))
print(list_to_set([1, 1, 2, 2, 3, 3]))
print(list_to_set([1, 2, 3, 4, 5, 5, 5, 3, 4, 5]))

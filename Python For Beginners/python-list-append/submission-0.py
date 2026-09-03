# We can also add new elements to the end of a list using the append() function. 
# The append() function adds an element to the end of the list. This is not a separate function, it's called with a period after the list name (.append()). This is called a method. It is a function that is associated with a specific object (in this case, a list is an object).

from typing import List # this is used to add type hints for List type

def append_to_list(my_list: List[int], elements: List[int]) -> List[int]:
    for i in elements:
        return my_list.append(i)

# do not modify below this line
print(append_to_list([1, 2, 3], [4, 5]))
print(append_to_list([], [1, 2, 3, 4]))

# Tuples are very similar to lists, but they have one key difference: they are immutable. This means that once a tuple is created, it cannot be changed. We can create a tuple by using parentheses instead of square brackets.
# We also can't call append or pop on a tuple, since these functions would modify it. We can however still call sum(), max(), and min() on a tuple, since these functions don't modify the tuple.

from typing import Tuple # this is to add type hints for tuples

def create_pair(name: str, age: int) -> Tuple[str, int]:
    nat = (name, age)
    return nat

# do not modify code below this line
print(create_pair("Alice", 25))
print(create_pair("Bob", 30))
print(create_pair("Charlie", 35))
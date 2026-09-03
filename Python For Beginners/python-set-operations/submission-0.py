# We can remove elements from a set using the remove() function.
# We can also convert a list into a set by passing the list into the set() function. We can then convert the set back into a list by passing it into the list() function. This is an easy way to remove duplicates from a list.

from typing import List

def count_unique_words(words: List[str]) -> int:
    myset = set(words)
    return len(myset)

# do not modify code below this line
print(count_unique_words(["hello", "world", "hello", "goodbye"]))
print(count_unique_words(["hello", "world", "i", "am", "world"]))
print(count_unique_words(["hello", "hello", "hello"]))
print(count_unique_words([]))
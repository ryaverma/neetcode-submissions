from typing import List

def contains_duplicate(words: List[str]) -> bool:
    listlen = len(words)
    myset = set(words)
    setlen = len(myset)
    if listlen==setlen:
        return False
    else:
        return True

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))

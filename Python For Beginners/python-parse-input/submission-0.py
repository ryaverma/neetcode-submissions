# Sometimes we have to do more than just convert the input to a single type. We might need to restructure the input in some way. This is called parsing the input.

from typing import List

def read_integers() -> List[int]:
    read = input()
    print(read.split(','))

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())

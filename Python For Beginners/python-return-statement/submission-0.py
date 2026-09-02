# Functions are even more extensible than they seem. Instead of just printing a value, you can also return a value from a function. This allows you to use the result of a function in other parts of your code, outside of the original function.

def product(n1, n2):
    return n1*n2

# don't modify below this line
print(product(2, 4))
print(product(8, 2))
print(product(4, 8))
print(product(8, 8))

# In programming, the scope refers to the visibility or accessibility of variables within different parts of the code. The value 11 passed into the print_number() function, is only accessible within the function. The function has its own scope, and the variable n inside the function is a different variable than the one outside the function. This is why the value of the original n is still 10 after the function call.

def add_one(n):
    n = n + 1
    print(n)   

n = 10

add_one(n)     # Output: 11

print(n)       # Output: ?

# Global Scope:
# Variables declared outside of any function have a global scope.
# They can be accessed from anywhere in the program, including inside functions.
# Local Scope:
# Variables declared within a function have a local scope.
# They can only be accessed within the function in which they are defined.
# Local variables are created when the function is called and destroyed when the function exits.


n = 100

def print_local_variable(num: int) -> None:
    print(num)

print_local_variable(n)

print(n)

# We can also use slicing to reverse a string. By not specifying the starting index or the ending index, and setting the step to -1, the string will be reversed.

def reverse_string(input_string: str) -> str:
    return input_string[::-1]

# do not modify below this line
print(reverse_string("NeetCode"))
print(reverse_string("Hello!"))
print(reverse_string("Bye Bye"))

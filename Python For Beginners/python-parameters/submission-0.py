# You may have noticed that when we call the print() function, we put variables and strings inside of the parentheses. That's because a function can be defined with parameters. When calling a function, you can pass values, variables, or expressions as arguments to the function.

# A parameter is a variable in a function definition. When a function is called, the arguments are the data you pass into the function's parameters. In the example above, the parameter is name and the argument is "Alice".

def farewell(name):
    print("Goodbye, "+name)

farewell("Bob")
farewell("Charlie")
# don't modify below this line
farewell("NeetCode")

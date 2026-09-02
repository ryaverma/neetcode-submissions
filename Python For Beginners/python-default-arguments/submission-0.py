# You can specify default values for parameters in a function definition. Example, we have given the parameter name a default value of "world". If we call the function without any arguments, the default value will be used. If we call the function with an argument, that argument will be used instead. We can also have multiple parameters with default values. But the order of the parameters matters! If you have a parameter with a default value, all parameters after it must also have default values.

def greet(name, punctuation="!") -> None:
    print("Hello, " + name + punctuation)

greet("World", "!")
greet("World")

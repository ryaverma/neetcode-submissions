# To add a type hint for a parameter, you add a colon after the parameter name and then the type of data you expect. To add a return type, you add a right arrow (->) after the closing parenthesis and then the type of data you expect to return (before the colon).

def greet(name: str) -> None:
    print("Hello, " + name)

result = greet("NeetCode")
print(type(result))


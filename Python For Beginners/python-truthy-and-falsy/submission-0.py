# Python has the concept of truthy and falsy values. A value is considered truthy if it evaluates to True in a boolean context. A value is considered falsy if it evaluates to False in a boolean context. The condition in an if statement is considered a boolean context.
# A value is falsy if it is:
# False (boolean)
# None (NoneType)
# 0 (integer)
# 0.0 (float)
# "" (empty string)
# [] (empty list)
# Most other empty collections (e.g. empty tuple, empty set, empty dictionary)
# A value is truthy if it is:
# True (boolean)
# All integers other than 0
# All floats other than 0.0
# All strings other than ""
# All collections with at least one element

def is_truthy(value) -> str:
    if value:
        return "Truthy"
    else:
        return "Falsy"


# don't modify code below this line
print(0, "is", is_truthy(0))
print(10, "is", is_truthy(10))

print(0.0, "is", is_truthy(0.0))
print(10.0, "is", is_truthy(10.0))

print("empty str", "is", is_truthy(""))
print("non-empty str", "is", is_truthy("non-empty str"))

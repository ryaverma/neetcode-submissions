# Python provides a way to format strings using the format method. We then call the format method on the string and pass in the values we want to replace the placeholders with. 
# The values are passed in the order they are to be inserted. The number of placeholders must match the number of arguments passed to the format method.
# An even more concise way to format strings is to use f-strings. These are prefixed with an f before the string and allow you to insert variables directly into the string.

def say_goodbye(name: str, hour: int) -> str:
    return "Goodbye, {}. See you again at {} o'clock.".format(name, hour)
    # return "Goodbye, {1}. See you again at {0} o'clock.".format(hour, name)
    # return "Goodbye, {name}. See you again at {hour} o'clock."

# do not modify below this line
print(say_goodbye("Bob", 12))
print(say_goodbye("Jane", 4))
print(say_goodbye("NeetCode", 9))

# Python allows you to assign multiple variables in a single line. Just separate the variables with a comma, and the right-hand side values with a comma as well. We can also use this to swap the values of variables.

msg1, msg2 = "World", "Hello"
msg3, msg4, msg5 = "Name", "Is", "My"
# Don't change the code above this line

msg1, msg2 = msg2, msg1
msg3, msg4, msg5 = msg5, msg3, msg4


# Don't change the code below this line
print(msg1)
print(msg2)
print(msg3)
print(msg4)
print(msg5)

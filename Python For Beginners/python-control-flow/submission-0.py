# Python provides control statements to alter the execution of loops.
# break: Exits the loop immediately.
# continue: Skips the remaining code inside the loop for the current iteration and moves to the next iteration.
# pass: Acts as a placeholder and does nothing. We cannot have empty loops, so we use pass to avoid errors. It can also be used in conditional statements and functions.

for i in range(1, 8):
    pass

if True:
    pass

def unfinsished_function():
    pass

for i in range(1, 8):
    break
    print(i)

for i in range(1, 8):
    continue
    print(i)

print("nothing else happened")

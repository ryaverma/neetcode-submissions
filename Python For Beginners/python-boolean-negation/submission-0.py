# not operator simply inverts the value of the operand. If the operand is True, the result is False. If the operand is False, the result is True

a, b, c = False, False, True
print(not a)
print(not c)
print(not(a and b))
print(not(b or c))
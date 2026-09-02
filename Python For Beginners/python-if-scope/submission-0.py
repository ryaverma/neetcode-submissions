# Unlike functions, if statements do not create a new scope. This means that variables defined inside an if statement are accessible outside of the if statement. Within functions, if statements have the same scope as the function. This means that variables defined inside an if statement are accessible within that function, but not outside of it.

def pay_bill(balance: int, bill: int) -> int:
    if balance>=bill:
        return balance-bill
    return balance

# do not modify below this line
print(pay_bill(100, 50))
print(pay_bill(100, 100))
print(pay_bill(100, 150))

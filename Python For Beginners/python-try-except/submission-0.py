# When an error occurs in a program, it usually causes the program to crash. But there is a way we can handle these errors and prevent the program from crashing. This is done using the try and except blocks.
# A try block is reminiscent to an if-else statement. The code inside a try block is always executed, but if any line of code raises an error, the program will immediately jump to the except block. If no error occurs, the except block is skipped. This is called exception handling.

def divide_numbers(a: int, b: int) -> None:
    try:
        result = a/b
        print(result)
    except:
        print("An error occurred!")

# do not modify below this line
divide_numbers(10, 2)
divide_numbers(12, 3)
divide_numbers(2, 0)

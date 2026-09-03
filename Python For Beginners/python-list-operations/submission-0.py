# Lists can also be used within conditional statements. We can also use the in operator to check if an element is present in a list. If we want to check if an element is not in the list, we can use the not in operator.

def check_list_empty(my_list) -> bool:
    if my_list:
        return True


def check_element_in_list(my_list, element) -> bool:
    if element in my_list:
        return True

# do not modify below this line
print(check_list_empty([]))
print(check_list_empty([1, 2, 3]))

print(check_element_in_list([1, 2, 3], 1))
print(check_element_in_list([1, 2, 3], 4))

print(check_element_in_list(["Apple", "Banana", "Orange"], "Banana"))
print(check_element_in_list(["Apple", "Banana", "Orange"], "Grape"))

def add_two_numbers() -> int:
    nums = input()
    nums_split = nums.split(",")
    add_num = 0
    for i in nums_split:
        add_num += int(i)
    return add_num

# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())

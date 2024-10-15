def split_list(lst):
    if len(lst) == 0:
        return [[], []]
    middle = (len(lst) + 1) // 2
    first_part = lst[:middle]
    second_part = lst[middle:]
    return [first_part, second_part]
numbers = [5, 6, 2, 1, 6]
new_list = split_list(numbers)
print(new_list)
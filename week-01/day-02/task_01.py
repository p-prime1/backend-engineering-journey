numbers = [10, 5, 8, 20, 3, 15]

def second_largest_number(number: list):
    """Find the second-largest number."""
    first_large_number = number[0]
    second_list = number[:]

    for _ in number:
        if _ > first_large_number:
            first_large_number = _
    print(first_large_number)
    second_list.remove(first_large_number)
    second_large_number = second_list[0]
    for _ in second_list:
        if _ > second_large_number:
            second_large_number = _
    print(second_large_number)
second_largest_number(numbers)

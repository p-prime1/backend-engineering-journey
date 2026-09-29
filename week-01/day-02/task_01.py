numbers = [10, 5, 8, 20, 3, 15]

def second_lowest_number(number: list):
    """Find the second-largest number."""
    first_low_number = 0
    second_low_number = 0
    second_list = number[:]

    for _ in number:
        if _ > first_low_number:
            first_low_number = _
    print(first_low_number)
    second_list.remove(first_low_number)
    for _ in number:
        if _ > second_low_number:
            second_low_number = _
    print(second_low_number)
second_lowest_number(numbers)

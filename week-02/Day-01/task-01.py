numbers = [12, 7, 4, 19, 8, 7, 12, 3]

def number_inspector(num: list):
    largest_num = 0
    smallest_num = num[0]
    count = 0
    even_list = []

    for _ in num:
        if _ < smallest_num:
            smallest_num = _
        if _ > largest_num:
            largest_num = _
        if _ ==  7:
            count += 1
        if _ % 2 == 0:
            even_list.append(_)
    print(largest_num, smallest_num, count, even_list)

number_inspector(numbers)



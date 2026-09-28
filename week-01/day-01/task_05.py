new_list = [4, 7, 2, 9, 1, 7, 4, 8]
repeated_num = []
count = 0
for _ in new_list:
    for i in new_list:
        if i == _:
            count += 1
    if count > 1:
        if _ in repeated_num:
            pass
        else:
            repeated_num.append(_)
    count = 0
print(repeated_num)

repeated_list = []
for _ in new_list:
    if new_list.count(_) > 1:
        if _ not in repeated_list:
            repeated_list.append(_)
print(repeated_list)

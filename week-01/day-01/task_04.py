def square(number:int):
    return(number * number)

def largest_number(new_list:list):
    temp = new_list[0]
    for _ in new_list:
        if temp < _:
            temp = _
        else:
            pass
    return temp

x = int(input("input number: "))
print(square(x))
y = list(map(int, input("Input list: ").split(',')))
print(largest_number(y))

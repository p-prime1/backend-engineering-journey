text = "backend engineering"
def char_count(text):
    new_set = {i for i in text}
    new_set.remove(' ')
    new_dict = {}
    for i in new_set:
        new_dict[i] = 0
    for _ in new_set:
        for i in text:
            if _ == i:
                new_dict[_] += 1
    print(new_dict)

char_count(text)

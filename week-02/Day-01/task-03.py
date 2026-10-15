text = "backend engineering"

new_list = list(text)
new_list.remove(" ")
new_dict = dict()

for _ in new_list:
    new_dict[_] = 0
for _ in new_list:
    new_dict[_] += 1
print(new_list)
print(new_dict)

new_list = ["1G", "2G", "3G", "4G", "5G"]

print(new_list)
for _ in new_list:
    print(_)
new_list.append("6G Future Gen")
last_tech = new_list.pop()
print(last_tech)

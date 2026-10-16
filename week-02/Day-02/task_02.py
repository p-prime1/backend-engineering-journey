with open("notes.txt", "w") as f:
    f.write("Hello World")

with open("notes.txt", "r") as f:
    print(f.read())

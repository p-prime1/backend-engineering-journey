num = int(input("Input number: "))

if num < 0:
    print(f"{num} is a negative number")
elif num > 0:
    print(f"{num} is a positive numnber")
    if num % 2 == 0:
        print(f"and is an even number")
    else:
        print(f"and is an odd number")

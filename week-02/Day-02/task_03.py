def safe_divide(a: int, b: int):
    try:
        value = a / b
    except ZeroDivisionError as e:
        print(e)
    except TypeError as e:
        print(e)
    else:
        return value


safe_divide(10, 2)
safe_divide(10, 0)
safe_divide("ten", 2)

def spam(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError:
        print("Invalid argument")
print(spam(0))
print(spam(2))
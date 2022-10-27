from unittest import result


def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("You can't divide by zero")
    except TypeError:
        print("Data type not supported")
    else:
        return result
    finally:
        print("Inside Finally")


a = 1
b = 2
print(divide(a, b))

a = 5
b = 0
print(divide(a, b))
a = "5"
b = "2"
print(divide(a, b))

for i in range(10):
    print(i)
    break
else:
    print("Inside else")

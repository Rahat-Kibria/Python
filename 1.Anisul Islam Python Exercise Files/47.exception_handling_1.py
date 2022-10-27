try:
    list = [20, 0, 30]
    result = list[0]/list[3]
    print(result)
    print("done")
except ZeroDivisionError:
    print("Cannot be divided by 0")
except IndexError:
    print("Index Error")
finally:
    print("Codes in finally will be executed")
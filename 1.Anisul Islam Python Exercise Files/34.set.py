num1 = {1, 2, 3, 4, 5}
num2 = set([4, 5, 6, 7])
num2.add(8)
num2.remove(8)
print(num2)
print(8 in num2)
print(4 in num2)
print(8 not in num2)
print(num1 | num2) # union set
print(num1 & num2) # intersection set
print(num1 - num2) # difference set
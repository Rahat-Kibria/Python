# map alternative
num = [1, 2, 3, 4, 5]
result = [x*x for x in num] # [] is meant for list
print(result)

# filter alternative
result = [x for x in num if x % 2 == 0]
print(result)
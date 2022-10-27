# 1+2+3+...+n
# sum = 0
n=int(input("Enter the last number: "))
# for x in range(1, n + 1, 1):
#     sum = sum + x
# print(sum)

# 2+4+6+...+n
# for x in range(2, n + 1, 2):
#     sum = sum + x
# print(sum)

# 1*1 + 2*2 + 3*3 +...+ n*n
# for x in range(1, n + 1, 1):
#     sum = sum + x * x
# print(sum)

# 1 + 1/2 + 1/3 +...+ 1/n
# for x in range(1, n + 1, 1):
#     sum = sum + 1 / x
# print(sum)

# 1 * 2 * 3 *...* n
sum = 1
for x in range(1, n + 1, 1):
    sum = sum * x
print(sum)
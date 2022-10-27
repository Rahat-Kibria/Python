def fnc(x, li):
    print('type of x: ', type(x))
    print('type of li: ', type(li))

    x = 500
    li.append(4)

    return x


a = 10
my_li = [1, 2, 3]
print('List before function call: ', my_li)
y = fnc(a, my_li)

print('Value of y: ', y)
print('Value of a: ', a)
print('List after function call: ', my_li)

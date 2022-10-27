# xargs
# ================
# def student(*details):
#     print(details)
# student("Rahat", 29, 3.53)

# def add(*numbers):
#     sum = 0
#     for num in numbers:
#         sum = sum + num
#     print(sum)
# add(10, 20)
# add(10, 20, 30)

# xxargs
# ================
def student(**details):
    # print(details)
    print(details["name"])
student(id = 101, name = "Rahat")
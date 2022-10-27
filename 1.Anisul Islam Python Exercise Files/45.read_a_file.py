file = open("45.student.txt", "r")
# print(file.readable())
# text = file.read()
# print(text)
# size = len(text)
# print(size)
# text2 = file.readlines()
# text2 = file.readlines()[0]
# print(text2)
for line in file:
    print(line)
file.close()
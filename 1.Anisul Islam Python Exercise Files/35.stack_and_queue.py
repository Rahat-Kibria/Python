# Stack
# ==================
# books = []
# books.append("C")
# books.append("C++")
# books.append("Java")
# print(books)
# books.pop()
# print("Now the top book is :", books[-1])
# books.pop()
# print("Now the top book is :", books[-1])
# books.pop()
# if not books:
#     print("No books found")

# Queue
#==================
from collections import deque
persons = deque(["Rahat", "Hasan", "Salma"])
print(persons)
persons.popleft()
print(persons)
persons.popleft()
persons.popleft()
if not persons:
    print("No person left")

"""
n=3
*
**
***
"""
# n = 3
# for i in range(n+1):
#     print(i*"*")

"""
n=3
*
***
*****
"""
# n = 3
# for i in range(n+1):
#     print((2*i-1)*"*")

"""
n=3
  *
 **
***
"""
rows = 3
k = 2 * rows - 2
for i in range(0, rows):
    # process each column
    for j in range(0, k):
        # print space in pyramid
        print(end=" ")
    k = k - 2
    for j in range(0, i + 1):
        # display star
        print("* ", end="")
    print("")

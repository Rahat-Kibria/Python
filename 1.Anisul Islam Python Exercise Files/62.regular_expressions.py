import re
pattern = r"Color"
# pattern = r"Col"
# if re.match(pattern, "Color is Color, I love red Color"):
#     print("Match")
# else:
#     print("Not matched")

# if re.search(pattern, "Red is a Color, I love red Color"):
#     print("Match")
# else:
#     print("Not matched")

# print(re.findall(pattern, "Red is a Color, I love red Color"))

text = "Red is a Color, I love red Color"
match = re.search(pattern, text)
if match:
    print(match.start())
    print(match.end())
    print(match.span())

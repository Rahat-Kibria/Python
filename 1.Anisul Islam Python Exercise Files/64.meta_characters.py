from ast import pattern
import re
# pattern = r"col..r"
# pattern = r"^col..r$"
# pattern = r"a*"  # 0 or more a character to be matched
# pattern = r"a+"  # 1 or more a character to be matched
# pattern = r"col(-)our"  # it checks col-our
# pattern = r"col(-)?our"  # it checks col-our or colour
pattern = r"a{1,3}"  # it checks 1-3 a charater to be matched
if re.match(pattern, "colour"):
    print("Matched")
# if re.match(pattern, "col-our"):
#     print("Matched")

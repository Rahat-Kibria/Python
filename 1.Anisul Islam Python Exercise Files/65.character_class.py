from ast import pattern
import re
# pattern = r"[aeiou]"  # checking for vowel characters
pattern = r"[A-Z][a-z][0-9]"  # checking for first characters
# serials have to be maintained
# if re.match(pattern, "acolour"):
#     print("Matched")
if re.match(pattern, "Ab8blah"):
    print("Matched")

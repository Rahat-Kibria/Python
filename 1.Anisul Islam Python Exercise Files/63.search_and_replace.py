from ast import pattern
from cgitb import text
import re
pattern = r"colour"
text1 = "My favorite colour is Red. I love blue colour as well"
# text2 = re.sub(pattern, "color", text1)
text2 = re.sub(pattern, "color", text1, count=1)
print(text2)

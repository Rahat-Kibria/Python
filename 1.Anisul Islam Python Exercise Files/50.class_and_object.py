class Student:
    roll = ""
    gpa = ""
rahim = Student()
# print(isinstance(rahim, Student))
rahim.roll = 101
rahim.gpa = 3.234
print(f"Roll: {rahim.roll}, GPA: {rahim.gpa}")

kahim = Student()
kahim.roll = 102
kahim.gpa = 3.676
print(f"Roll: {kahim.roll}, GPA: {kahim.gpa}")
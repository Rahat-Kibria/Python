class Student:
    roll = ""
    gpa = ""
    def setValue(self, roll, gpa):
        self.roll = roll
        self.gpa = gpa
    def display(self):
        print(f"Roll: {self.roll}, GPA: {self.gpa}")
rahim = Student()
rahim.setValue(101, 3.343)
rahim.display()
karim = Student()
karim.setValue(102, 3.656)
karim.display()

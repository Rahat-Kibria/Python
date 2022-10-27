# Multilevel Inheritance
# ==========================

class A:
    def display1(self):
        print("I am inside A class")


class B(A):
    def display2(self):
        print("I am inside B class")


class C(B):
    def display3(self):
        super().display1()
        super().display2()
        print("I am inside C class")


obj = C()
obj.display3()

# Multiple Inheritance
# ==========================


class X:
    def display(self):
        print("I am inside X class")


class Y:
    def display(self):
        print("I am inside Y class")


class Z(X, Y):
    pass


obj2 = Z()
obj2.display()

class Employee:  # Parent Class
    def intro(self):
        print("Employee introduction")


# child class Emp1 inherits the base class Employee


class Emp1(Employee):  # Child Class
    def rank(self):
        print("I am Director ")


p1 = Emp1()

p1.rank()

p1.intro()

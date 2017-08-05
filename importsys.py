import sys
print(sys.executable)
print(sys.version)


class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def email(self):
        return "{}.{}@email.com".format(self.first, self.last)

    def __repr__(self):
        return repr(self.first + " " + self.last)


emp_1 = Employee("John", "Smith")


print(emp_1)

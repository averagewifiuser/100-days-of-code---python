#magic methods
class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last+ '@companyemail.com'

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self): #unambigous rep of the obj, meant for other devs (use something that can be use to recreate the obj)
        return f"Employee({self.first}, {self.last}, {self.pay})"

    def __str__(self): #readble for end users
        return f"{self.fullname()} - {self.email}"



emp_1 = Employee("Test", "User", 90000)
emp_2 = Employee("Another", "User", 80000)

print(emp_1)
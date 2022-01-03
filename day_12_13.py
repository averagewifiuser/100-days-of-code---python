#Python OOP

class Employee:
    
    #class variable
    raise_amount = 1.04
    num_of_emps = 0

    #constructor
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"

        #this is a class var that needs to be constant for all instances and there's no use case that
        #would need it overridden
        Employee.num_of_emps += 1

    #regular methods
    def fullname(self):
        return f"{self.first} {self.last}"

    
    def apply_raise(self):
        self.pay = int(self.pay + self.raise_amount)

    
    #class methods
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
    

    #alt constructor
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    
    #staticmethods
    #used for logical connections to the class (no real relation gidigidi to the class)
    #if you don't use anything of the class (variables, self, or cls then use a staticmetod)
    @staticmethod
    def is_work_day(day):
        #5 is staturay
        #6 is sunday, issa datetime convention
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

#instancee variables are particular to that instance
emp_1 = Employee('Man', 'Dingo', 90000)
emp_2 = Employee('Test', 'Dingo', 201000)


Employee.set_raise_amt(1.06)

print(Employee.raise_amount)
print(emp_2.raise_amount)
print(emp_1.raise_amount)
# emp_1.first = 'Man'
# emp_1.last = 'Dingo'
# emp_1.pay = 40000

# emp_2.first = 'Test'
# emp_2.last = 'Dingo'
# emp_2.pay = 40000

# print(emp_1.fullname())
# print(Employee.fullname(emp_2))
# print(emp_2.email)

#class variables are te same for all of them

#alt constructor with classmethod
emp_str_1 = 'John-Doe-9000'
emp_str_2 = 'Jane-Die-91212'

new_emp_1 = Employee.from_string(emp_str_2)

import datetime
my_date = datetime.datetime.now()

print(Employee.is_work_day(my_date))

print(new_emp_1.email)

'''class variables'''


class Employee:
    num_of_emps = 0
    raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '_' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self): # dont forget self <-
        return "{} {}".format(self.first, self.last)
    


    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt) 
           

emp_1 = Employee("corey","Schafer", 50000)
emp_2 = Employee("test","user", 60000)







#print(Employee.raise_amt())
print(emp_1.raise_amt)
print(emp_2.raise_amt)
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(emp_1.last)
print(emp_1.email)
'''print(Employee.__dict__)
print(emp_1.__dict__)
print(Employee.num_of_emps)
Employee.raise_amt = 1.05
emp_1.raise_amt = 1.05



print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

print(emp_1.raise_amt)
print(emp_1.apply_raise())


print(emp_1.apply_raise())

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)'''



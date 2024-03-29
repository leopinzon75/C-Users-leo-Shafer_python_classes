'''special methods'''


class Employee:
    
    
    def __init__(self, first, last, pay): 
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '_' + last + '@company.com'
 

    def fullname(self): # dont forget self <-
        return "{} {}".format(self.first, self.last)
    
    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.email, self.fullname())

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())



emp_1 = Employee("corey","Schafer", 50000)
emp_2 = Employee("test","user", 60000)

print(emp_1.__repr__())


print(len(emp_1))
print(len('test'))
print('test'.__len__())


print(emp_1 + emp_2)


print(emp_1)
print(repr(emp_1))
print(str(emp_1))


print(emp_1.__repr__())
print(emp_1.__str__())
print(emp_2.fullname())

print(1+2)

print(int.__add__(1, 2))
print(str.__add__('a', 'b'))






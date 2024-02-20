'''class methods and static methods'''


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
    
    def kkkk(self): #bard
        raise_amount = int(self.pay * self.raise_amt) - self.pay
        return raise_amount

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def total_percent(self):              #mine
        total_percent = int(self.pay * self.raise_amt)
        return total_percent
    
# A regular method automatically takes in the instance variable 'above', as the first argument, (self)
# then a class method takes in the class variable (cls) as the first argument , and to turn it into 
# is as easy as adding a decorator to the top, called class method 'below'
    
# A decorator alters the functionality of our method, where now we receive the 
# class as our first argument (cls) instead of oour instance (self) 
    
    @classmethod # Decorator 
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount


    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)



    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    
# import datetime
# my_date = datetime.date(2016, 7, 11)

# print(Employee.is_workday(my_date))

emp_1 = Employee("corey","Schafer", 50000)
emp_2 = Employee("test","user", 60000)

#Employee.set_raise_amt(1.05)
emp_1.set_raise_amt(1.05)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)






# emp_str_1 = 'john-doe-70000'
# emp_str_2 = 'steve-smith-30000' 
# emp_str_3 = 'Christine-Jhonson-90000'

# first, last, pay = emp_str_1.split('-')
# new_emp_1 = Employee(first, last, pay)



# new_emp_3 = Employee.from_string(emp_str_3)
# new_emp_2 = Employee.from_string(emp_str_2)
# new_emp_1 = Employee.from_string(emp_str_1)


# print(Employee.fullname(new_emp_3)) 
# print(Employee.fullname(new_emp_2)) 
# print(Employee.fullname(new_emp_1)) 
# print(emp_1.pay)
# #emp_1.apply_raise()
# print(emp_1.pay)
# #print(emp_1.apply_raise())
# print(emp_2.kkkk())

# #print(Employee.num_of_emps)
# # print(Employee.__dict__)


# '''new_emp_1 = Employee.from_string(emp_str_1) 
# new_emp_2 = Employee.from_string(emp_str_2) 
# new_emp_3 = Employee.from_string(emp_str_3)
# print(emp_2.kkkk())
# print(emp_1.total_percent())
# print(emp_1.apply_raise())'''
 
# '''
# print(new_emp_1.fullname())
# print(new_emp_1.email)
# print(new_emp_1.pay)
# print(emp_1.kkkk())

# print(new_emp_1.__dict__)

# print(new_emp_2.fullname())
# print(new_emp_2.email)
# print(new_emp_2.pay)
 
# print(new_emp_2.__dict__)


# print(new_emp_2.fullname())
# print(new_emp_3.email)
# print(new_emp_3.pay)
# print(new_emp_2.__dict__)'''

# '''
# #print(Employee.num_of_emps)
# print(new_emp_3.fullname())
# print(new_emp_3.email)
# #print(emp_1.set_raise_amt())
# #Employee.set_raise_amt  (1.05)
# new_emp_3 = Employee(first, last, pay)'''


# #emp_1.apply_raise()
# #print(emp_1.pay)

# #emp_1.raise_amount
# #print( Employee.set_raise_amt())
# '''
# new_emp_3 = Employee.from_string(emp_str_3)

# print(new_emp_3.fullname())
# print(Employee.num_of_emps)

# print(new_emp_3.email)
# print(new_emp_1.email)
# print(new_emp_1.email)'''

# '''def total_percent(self):
#         total_percent = int(self.pay * self.raise_amt)
#         return total_percent
#         self.pay = self.pay
#         total_percent = total_percent (self.pay)
#         print(total_percent)'''

# '''def apply_raise(self):
#         raise_amount = self.pay * self.raise_amt - self.pay
#         self.pay = int(self.pay * self.raise_amt)
#         return raise_amount'''
# '''    def kkkk(self):
#         raise_amount = int(self.pay * self.raise_amt) - self.pay
#         return raise_amount'''
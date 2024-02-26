 
class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)




# class Developer(Employee):
#     raise_amt = 1.10 # We can make this changes in the subclass without
                     #havig to worry of breaking the parents class

# dev_1 = Employee('Corey', 'Schafer', 50000)
# dev_2 = Developer('Test', 'Employee', 60000)
#
#
# print(dev_1.email)
# print(dev_2.email)

# print(dev_1.pay)# 50000
# dev_1.apply_raise()
# print(dev_1.pay)# 52000  # We can make this changes in the subclass without
                         #havig to worry of breaking the parents class


# To add more attributes internally into the subclass, for example programmin 
#languaje, we will do this:

class Developer(Employee):

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

# print(dev_1.email)
# print(dev_1.prog_lang)


# Instead of super you can also do this: Employee.__init__(self, first, last, pay)



# Now let's create another subclass called manager with new functions:
# In this class we are going to provide a list of employees that the manager supervises
# at the init method and equal to none

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):# Do not pass a mutable data type as default argument
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

# Methods to add and remove employees that our manager supervises:

    def add_dev(self, dev):
        if dev not in self.employees:
            self.employees.append(dev)# Attention of 3 words together with dot notation = 2 dots in the statement

    def remove_dev(self, dev):
        if dev in self.employees:
            self.employees.remove(dev)
  


# To print out all of the employees that the manager supervises
            
    def print_devs(self):
        for dev in self.employees:
            print('-->', dev.fullname())

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])# Here is where we find the list created at the init method

# print(mgr_1.email)# Sue.Smith@email.com
mgr_1.print_devs()# --> Corey Schafer 
mgr_1.add_dev(dev_2)# --> Test Employee
mgr_1.print_devs()#---> Corey Schafer
# mgr_1.remove_emp(dev_2)# user1s-MacBook-Pro:Shafer_Python_Classes admin$ /usr/local/bin/python3 /Users/admin/Desktop/Shafer_Python_Classes/4-Inheritance/oop.py













# print(help(Developer))
#  |      Employee
#  |  
#  |  Method resolution order:
#  |      Developer
#  |      Employee
#  |      builtins.object
#  |   
#  |  Methods inherited from Employee:
#  |  
#  |  __init__(self, first, last, pay)
#  |      Initialize self.  See help(type(self)) for accurate signature.
#  |  
#  |  apply_raise(self)
#  |  
#  |  fullname(self)
#  |  
#  |  ----------------------------------------------------------------------
#  |  Data descriptors inherited from Employee:
#  |  
#  |  __dict__
#  |      dictionary for instance variables (if defined)
#  |  
#  |  __weakref__
#  |      list of weak references to the object (if defined)
#  |  
#  |  ----------------------------------------------------------------------
#  |  Data and other attributes inherited from Employee:
#  |  
#  |  raise_amt = 1.04





# print(dev_1.raise_amt)
# dev_1.apply_raise()
# print(dev_1.raise_amt)


mgr_1.print_emps()
mgr_1.add_emp(dev_1)
mgr_1.print_emps()
mgr_1.print_emps()
print(mgr_1.email)
#Manager.print_emps(dev_1)
 


print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))
print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))

#mgr_1.remove_emp(dev_1)

mgr_1.print_emps()
mgr_1.add_emp(dev_1)
mgr_1.print_emps()

#Manager.print_emps(dev_2)





print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
print(dev_1.email)
print(dev_1.prog_lang)


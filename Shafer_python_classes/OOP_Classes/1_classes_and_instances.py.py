  # '''creating classes'''


# class Employee:
    
#     def __init__(self, first, last, pay): 
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '_' + last + '@company.com'
 

#     def fullname(self): # dont forget self <-
#         return "{} {}".format(self.first, self.last)
    
# emp_1 = Employee("corey","Schafer", 50000)
# emp_2 = Employee("test","user", 60000)

# print(emp_1.fullname())
# print(Employee.fullname(emp_1))
# print(emp_2.fullname())

# Note that we can create our instances without the init method, for example:

# emp_1.first = 'Corey'
# emp_1.last = 'Shafer'
# emp_1.email = 'Corey.Shafer@company.com'
# emp_1.pay = 50000
    
  
# emp_2.first = 'Test'
# emp_2.last = 'User'
# emp_2.email = ' Test.user@company.com'
# emp_2.pay = 60000

 

# print(emp_1.last)
# print(emp_1.email)
# print(emp_1.pay)
# w = emp_1.pay
# print(w)
# print(Employee.__dict__)

#print(emp_1.__dict__)
#print(w)
#print(emp_1.pay)
#print(emp_2.pay)

#print(emp_1.email)
#print(emp_2.email)

#print("{} {}".format(emp_1.first, emp_1.last))


#print(emp_2.fullname())
#print(Employee.__dict__)
#print(emp_2.__dict__)
#help(emp_1)

'''check bmi calculator to see assign of variables, name etc'''



#                    Updated class of this chapter from my github

# Python-Object-Oriented-Programming


# class Employee:
#     pass

# When you create methods within a class they receive the instance (self)
# as the first argument automatically, and after self we can specify what
# other arguments we want to accept

class Employee:
    def __init__(self, first, last, pay, a, b, c):# note on init:self d and h can be out but no errors
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + ',' + last + '@company.com'
        self.a = a
        self.b = b 
        self.c = c
        self.d = first + 'bbbb'
        self.h = last + 'gggg'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)



emp_1 = Employee('Corey', 'Shafer',  500000, 'a', 'b', 'c')# note on init: self d and h can be out but no errors
emp_2 = Employee('Test', 'User',  60000, 'a', 'b', 'c')

# print(emp_1.d)
# Output: Coreybbbb

# print(emp_1.a)
# Output: 
# a

# print(emp_1.h)
# Output: Shafergggg


# print(emp_1)
# print(emp_2)
        
    
# emp_1.first = 'Corey'
# emp_1.last = 'Shafer'
# emp_1.email = 'Corey.Shafer@company.com'
# emp_1.pay = 50000
    
  
# emp_2.first = 'Test'
# emp_2.last = 'User'
# emp_2.email = ' Test.user@company.com'
# emp_2.pay = 60000
      

# print(emp_1.email)
# print(emp_2.email)
  
# print('{} {}'.format(emp_1.first, emp_1.last))


# Use parentesis after the fullname method or you get this
#print(emp_1.fullname)
#Output: <bound method Employee.fullname of <__main__.Employee instance at 0x102df3248>>

print(emp_2.fullname())
# Output: Test User


# We can also run this methods using the class name

#print(Employee.fullname(emp_1))



# Basic code from original exercise:

# class Employee:

#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@company.com'
#         self.d = 'kkkkkk'

# emp_1 = Employee('Corey', 'Shafer',  500000,)
# emp_2 = Employee('Test', 'User',  60000,)

# print(emp_1.d) 

























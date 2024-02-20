'''# Functions are some instructions packaged together that performs specific tasks

def hello_func():
    pass


print(hello_func)# when pass is equal to <function hello_func at 0x0000017CF902B250> 
print(hello_func())# None
  
# use the function without need of printing because it was already declared

def hello_func():
     print('hello_function.')

hello_func()#hello_function.
hello_func()#hello_function.
hello_func()#hello_function.
hello_func()#hello_function.



# It allows to reuse code without repating ourselves
# Keep your code dry, do not repeat yourself

# "Return" allows to operate on some data and 
# then pass the results when the function is called

def hello_func():
     return'hello_function.'

hello_func()# No result when the code is runned.

print(hello_func())# hello_function.
# THink of a function as a machine that takes input and gives a result
# Be concern at the input and at the return value ex:

print(len('Test'))# 4, The function len, the input test and the return 4

# Once you get the output you can operate mehods and more on it based on its datatype

def hello_func():
     return'hello_function.'

hello_func()# No result when the caode is runned.

print(hello_func().upper()) #HELLO_FUNCTION. Once you get the output you can operate on it based on its datatype 
'''
# To be able to pass arguments into your function we need to crearte some 
# parameters inside of the parenthesis
# Let's customize the greeting of our function hello_func returns

# def hello_func(greeting):
#      return'{},function.'.format(greeting)

 
# print(hello_func())# TypeError: hello_func() missing 1 required positional argument: 'greeting'

# def hello_func(greeting):
#      return'{},function.'.format(greeting)
# print(hello_func('Hi'))  # Hi,function.

# def hello_func(greeting, name = 'you'):
#      return'{}, {} '.format(greeting, name)
# print(hello_func('Hi'))  # Hi, you 

# def hello_func(greeting, name = 'you'):
#      return'{}, {} '.format(greeting, name)
# print(hello_func('Hi', name = 'Corey'))# Hi, Corey 

# Positional and keyword arguments

# def student_info(*args, **kwargs):
#     print(args)# ('Math', 'Art')
#     print(kwargs)# {'name': 'John', 'age': 22}

# student_info('Math', 'Art', name = 'John', age = 22)

# ('Math', 'Art')
# {'cd': 'veinte', 'gf': 22}

# def student_info(*args, **kwargs):
#     print(args) # (['Math', 'Art'], {'name': 'John', 'age': 22})
#     print(kwargs) # {}

# courses = ['Math', 'Art']
# info = {'name': 'John', 'age': 22}

#student_info(courses, info )
# output: (['Math', 'Art'], {'name': 'John', 'age': 22})
#{}

# but if we include the * and the ** star at the arguments when calling the function

# def student_info(*args, **kwargs):
#     print(args)# ('Math', 'Art') 
#     print(kwargs)# {'name': 'John', 'age': 22}

# courses = ['Math', 'Art']
# info = {'name': 'John', 'age': 22}

# student_info(*courses, **info )

#output: ('Math', 'Art')
#{'name': 'John', 'age': 22} 

# Practice positional arguments
# def ab(*hi, **jk):
#     print(hi)
#     print(jk)

# ab('Math', 'Art', cd = 'veinte', gf = 22)

# ('Math', 'Art')
# {'cd': 'veinte', 'gf': 22}


# from the Python standard library:

# # Number of days per month. First value placeholder for indexing purposes.
# month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# def is_leap(year):
#     ''' Return leap for leap years, False for non-leap years.'''
#     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# def days_in_month(year, month):
#      '''Return number of days in that month in that year.'''

#      # year 2017
#      # month 2
#      if not 1 <= month <= 12:
#           return 'Invalid Month'
     
#      if month == 2 and is_leap(year):
#          return 29
     
#      return month_days[month]

# print(is_leap(20017))#False

# print(is_leap(2020))# True

# print(days_in_month(2017, 2))# 28

# print(days_in_month(2020, 2))# 29
   

#-----------------------------------------------------------------------------------------------------------

# gg = input() 
# print (type(gg))# <class 'str'>

# gg = list('45675')
# print (type(gg))    

# print(len(gg))
# print(gg[2])
















################practice
#practice integers

# b = 1 , 10

# for i in b:
#     print(i)    


# print(2%2)
# print(3%2)
# print(4%2)
# print(5%2)
# print(6%2)
# print(7%2)
# print(8%2)
# print(9%2)

# greeting = 'Hello'
# name = 'Michael'
# message = f'{greeting.upper()}, {name.lower()}. Welcome!'
# print(message)  


#practice lists


# courses = ['History', 'Math', 'Physics', 'CompSci']
# #courses.insert(0, 'Art')# ['Art', 'History', 'Math', 'Physics', 'CompSci']

# # print(courses.insert(0, 'Art'))#  None

# #print(courses.sort())# None
# # courses.sort()
# # # print(courses)
# # print(courses.index('CompSci')) 
# # print(courses.sort())
# # courses.sort()
# # print('Art' in courses)
# # for index, item in enumerate(courses, start = 1):
# #     print(index,item)

# course_str = ', '.join(courses)
# # print( print(courses))

# new_list = course_str.split( ', ' )
# print(course_str)
# print(new_list)

# c= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(c[:-1])


#practice strings

#message = 'Hello World'
# print(message.find('Universe'))

# #message = message.replace('World', 'Universe')

# message = 'Hello World'

# # message.replace('World', 'Universe')

# # print(message)

# message = message.replace('World', 'Universe')

# print(message)

# num = 2
# num *= 3.5647867464
# # print(type(num))



# courses = ['History', 'Math', 'Physics', 'CompSci']
# print(courses.index('Art'))# ValueError: 'Art' is not in list
# #print(courses.sort())
# #courses.sort()
# print(courses)
# cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
# Art_courses = {'History', 'Math', 'Art', 'Design'}

# print(cs_courses.intersection(Art_courses))# {'History', 'Math'}

# cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
# art_courses = {'History', 'Math', 'Art', 'Design'}

# print(cs_courses.difference(art_courses))# {'Physics', 'CompSci'}


# cs_courses = ['History', 'Math', 'Physics', 'CompSci']
# cs_courses.insert(0,'Art')
# print(cs_courses)

# cs_courses = ['History', 'Math', 'Physics', 'CompSci']
# art_courses = ['Art', 'Education']
# cs_courses.insert(0,art_courses)
# print(cs_courses[2])

# cs_courses = ['History', 'Math', 'Physics', 'CompSci']
# art_courses = ['Art', 'Education']
# cs_courses.extend(art_courses)
# print(cs_courses)


# cs_courses = ['History', 'Math', 'Physics', 'CompSci']
# art_courses = ['Art', 'Education']
# cs_courses.append(art_courses)
# print(cs_courses)

# cs_courses = ['History', 'Math', 'Physics', 'CompSci']
# cs_courses.insert(0, 'Art')
# print(cs_courses)


# nums = [1,5,2,4,3]




# art_courses = {'History', 'Math', 'Art', 'Design'}

# print(cs_courses.union(art_courses))# {'Physics', 'History', 'Design', 'Art', 'CompSci', 'Math'





#practice functions


# def ab(*hi, **jk):
#     print(hi)
#     print(jk)

# ab('Math', 'Art', cd = 'veinte', gf = 22)

# ('Math', 'Art')
# {'cd': 'veinte', 'gf': 22}


def student_info(*args, **kwargs):
    
    print(args)# ('Math', 'Art')
    print(kwargs)# {'name': 'John', 'age': 22}
    
courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

student_info( *courses, **info)
# It does not work if you put the print at the end
 













#comparison:
# == Equal to,
# != Not equal,
# > Greater than,
# < Less than,
# >= Greater or equal,
# >= Less or equal,
# is :  object identity  


# if True:
#     print('conditional was true')# 'conditional was true

# if False:
#     print('conditional was true')

# No output
 
-----------------------------------------------------------------------------------------

# language = 'Python'

# if language == 'Python':
#     print('language is Python')# language is Python
# else:
#     print('no match')

# No output

-----------------------------------------------------------------------------------------

# language = 'Java'

# if language == 'Python':
#     print('language is Python') # language is Python
# else:
#     print('no match')

# no match

-----------------------------------------------------------------------------------------
# language = 'Java'

# if language == 'Python':
#     print('language is Python')
# elif language == 'Java':
#     print('languaje is Java')# languaje is Java
# elif language == 'JavaScript':
#     print('languaje is JavaScript')
# else:
#     print('no match')

# = languaje is Java

-----------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------


# #and
# #or
# #not

# user = 'Admin'
# logged_in = True

# if user == 'Admin' and logged_in:
#     print('admin Page')# admin Page
# else:
#     print('Bad creds')

# = admin Page
-----------------------------------------------------------------------------------------


# user = 'Admin'
# logged_in = False

# if user == 'Admin' and logged_in:
#     print('admin Page')
# else:
#     print('Bad Creds')# Bad Creds

# = Bad Creds
-----------------------------------------------------------------------------------------

# user = 'Admin'
# logged_in = False

# if user == 'Admin' or logged_in:
#     print('admin Page')# admin Page
# else:
#     print('Bad Creds')

# = admin Page
-----------------------------------------------------------------------------------------

# user = 'Admin'
# logged_in = False

# if not logged_in:
#     print('Please Log in')# Please Log in
# else:
#     print('welcome')

#= Please Log in


-----------------------------------------------------------------------------------------
# Object identity : is.
# Tests if two objects have the same id in memory

# a = [1,2,3,]
# b = [1,2,3,]
# print(id(a))# 2563423218496
# print(id(b))# 2563423171904
# print(a is b) # False


 
# a = [1,2,3,]
# b = a
# print(id(a))# 2035798911808
# print(id(b))# 2035798911808
# print(a is b)# True
# print(a==b)# True
# print(id(a) == id(b))#True # This is the same of (a is b)


-----------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------

# To determine what Python evaluates to True and False,
# it's easier to show everything that evaluates to 'False', then everything else 
# will by default evaluate to True, we can use this quick 'if else statement' to test this

# # False values: 
    # False
    # None
    # Zero of any numeric type
    # Any empty secuence for example, ' ' , (), []. 
    # Any empty mapping, for example {}.

# condition = False

# if condition:
#     print('Evaluated to True')
# else:
#     print('Evaluated to False')# Evaluated to False

#= Evaluated to False

-----------------------------------------------------------------------------------------


# condition = None

# if condition:
#     print('Evaluated to True')
# else:
#     print('Evaluated to False')

# Evaluated to False

-----------------------------------------------------------------------------------------
# condition = 0

# if condition:
#     print('Evaluated to True')
# else:
#     print('Evaluated to False')# Evaluated to False

-----------------------------------------------------------------------------------------
# condition = 10

# if condition:
#     print('Evaluated to True')# Evaluated to True
# else:
# #     print('Evaluated to False')

-----------------------------------------------------------------------------------------
# condition = ()

# if condition:
#     print('Evaluated to True')
# else:
#     print('Evaluated to False')# Evaluated to False

-----------------------------------------------------------------------------------------
# condition = ['hdhdhdhdi']

# if condition:
#     print('Evaluated to True')# Evaluated to True
# else:
#     print('Evaluated to False')

-----------------------------------------------------------------------------------------
# condition = [ ]

# if condition:
#     print('Evaluated to True') 
# else:
#     print('Evaluated to False')# Evaluated to False     

-----------------------------------------------------------------------------------------
# condition = ''

# if condition:
#     print('Evaluated to True')
# else:
#     print('Evaluated to False')# Evaluated to False
 -----------------------------------------------------------------------------------------

# Now everything else pretty much is going to be evaluated to True



# condition = 'Test'

# if condition:
#     print('Evaluated to True')# Evaluated to True
# else:
#     print('Evaluated to False') 


import my_module
# run code  = Imported my_module...
courses = ['History', 'Math', 'Physics', 'CompSci']

index = my_module.find_index(courses, 'Math')
print(index)# 1 



# Make the module  name shorter:

# import my_module as mm
# # run code  = Imported my_module...
# courses = ['History', 'Math', 'Physics', 'CompSci']

# index = mm.find_index(courses, 'Math')
# print(index)# 1



# Importing the function itself: do not give access to the rest of the imported module

# from my_module import find_index
# # run code  = Imported my_module...
# courses = ['History', 'Math', 'Physics', 'CompSci']

# index = find_index(courses, 'Math')
# print(index)# 1    


# If you want access of extras into the module:

# from my_module import find_index, test
# # # run code  = Imported my_module...
# courses = ['History', 'Math', 'Physics', 'CompSci']

# index = find_index(courses, 'Math')
# print(index)# 1 
# print(test)# Test String         



# Making shorter the imported function:
# Do not rename if is not readable for the people

# from my_module import find_index as fi, test
# # # run code  = Imported my_module...
# courses = ['History', 'Math', 'Physics', 'CompSci']

# index = fi(courses, 'Math')
# print(index)# 1 
# print(test)# Test String

# #################################################################

# from my_module import find_index, test
# # # run code  = Imported my_module...
# courses = ['History', 'Math', 'Physics', 'CompSci']

# index = find_index(courses, 'Math')
# print(index)# 1 
# print(test)# Test String  

# A way of importing 'everything' instead to specify values and use commas
# but is not recommendable because we cannot identify what is in the module

# from my_module import *
# # # run code  = Imported my_module...
# courses = ['History', 'Math', 'Physics', 'CompSci']

# index = find_index(courses, 'Math')
# print(index)# 1 
# print(test)# Test String  


# To find a module python check multiple locations located in a list called sys.path

# from my_module import find_index, test
# import sys
# # run code  = Imported my_module...

# courses = ['History', 'Math', 'Physics', 'CompSci']

# index = find_index(courses, 'Math')
# print(sys.path)# ['c:\\Users\\leo\\Shafer_python_classes\\Pyhton _tutorial_for_beginners', 'C:\\Program Files\\Python310\\python310.zip',
# 'C:\\Program Files\\Python310\\DLLs', 'C:\\Program Files\\Python310\\lib', 'C:\\Program Files\\Python310',
# 'C:\\Users\\leo\\AppData\\Roaming\\Python\\Python310\\site-packages', 'C:\\Program Files\\Python310\\lib\\site-packages', 'C:\\Program Files\\Python310\\lib\\site-packages\\vboxapi-1.0-py3.10.egg']



# Now lets move my_module to desktop
  
# from my_module import find_index, test
# import sys
# # run code  = Imported my_module...

# courses = ['History', 'Math', 'Physics', 'CompSci']

# index = find_index(courses, 'Math')
# print(sys.path)# ModuleNotFoundError: No module named 'my_module'
  




# Now we can two different approaches:
# Manually add the directory or folder to sys.path


# import sys
# sys.path.append('/Users/leo/Desktop/my_modules')  

# from my_module import find_index, test
# # run code  = Imported my_module...

# courses = ['History', 'Math', 'Physics', 'CompSci']

# index = find_index(courses, 'Math')
# print(sys.path)    # ['c:\\Users\\leo\\Shafer_python_classes\\Pyhton _tutorial_for_beginners',
# # 'C:\\Program Files\\Python310\\python310.zip', 'C:\\Program Files\\Python310\\DLLs', 'C:\\Program Files\\Python310\\lib',
# # 'C:\\Program Files\\Python310', 'C:\\Users\\leo\\AppData\\Roaming\\Python\\Python310\\site-packages', 'C:\\Program Files\\Python310\\lib\\site-packages',
# # 'C:\\Program Files\\Python310\\lib\\site-packages\\vboxapi-1.0-py3.10.egg', '/Users/leo/Desktop/my_modules']

# print(index)# 1


# The second approach is making changes in the environment variable path
# The ways to do that it differs from windows to mac

# for a mac:pull up terminal
# set environment variables adding them to the
#dot bash underscore profile file in our homedirectory:

# $ nano ~/.bash_profile
#and at the end of the file:
# export PYTHONPATH="/Users/leo/Desktop/my_modules"
# CONTROL X AND 'Y' to save the file name
# restart the terminal and run:
# $ python
# import my_module
# import sys
# sys.path


# Now for windows:
# click on start button and type 'system properties"
#click advanced and at the bottom click on environmental variables
# click new on uppercase type PYTHONPATH
# Then the path of desktop "/Users/leo/Desktop/my_modules"
# click all okey, open the tmd, type python enter
#  import my_module
# import sys
# sys.path

# every text editor has documentation about python path



# Standard Libary: probably the function you are looking for is already there
# it is better to use it in production

# for example, we want to grab a random value from a list of values
# we  can use the random module from the standard library

# import random

# courses = ['History', 'Math', 'Physics', 'CompSci']
# random_course = random.choice(courses)

# print(random_course)# History    
 
# Another module from the standard library:

# import math

# rads = math.radians(90)

# print(rads)# 1.5707963267948966

# And if we want to get the sine:

# import math

# rads = math.radians(90)

# print(math.sin(rads))# 1.0




# Also the datetime and calendar modules

# import datetime
# import calendar

# # today = datetime.date.today()
# # print(today)# 2023-12-31

# # With the calendar module we can ask for leap years
# print(calendar.isleap(2023))# False

  
# # OS module it give us access to the underlying operatin system
# import os

# # to see what current directoty we are in
# print(os.getcwd())# C:\Users\leo



# These modules are files and we can see their loaction printing 
# their dunder file attribute

# import os
# print(os.__file__  )# C:\Program Files\Python310\lib\os.py

     
# import webbrowser
# import hashlib

# webbrowser.open('https://xkcd.com/353/')

# def geohash(latitude, longitude, datedow):
#     '''compute geohash() using the munroe algorithm.
#     >>>geodash(37,42154, -122,085589, b'2005-05-26-10458.68')
#     37.857713 - 122.544543
#     '''
#     # http://xkcd.com/426/
#     h = hashlib.md5(datedow).hexdigest()
#     p, q =[]
# import antigravity

  

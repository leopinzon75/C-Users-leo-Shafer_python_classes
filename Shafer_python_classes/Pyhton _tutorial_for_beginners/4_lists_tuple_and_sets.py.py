

# lists



# c= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(c[-1])# 10



# c= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(c[:-1])# [1, 2, 3, 4, 5, 6, 7, 8, 9]


c= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(c[:])


'''courses = ['History', 'Math', 'Physics', 'CompSci']

print(courses)

# Access values in a list 
courses = ['History', 'Math', 'Physics', 'CompSci']

print(len(courses)) #4

print(courses[0]) #History

print(courses[2]) #Physics

print(courses[-1]) #CompSci

#print(courses[4])
# Throws an error: index list out of range

# Up to but not included the entered digit 

 
courses = ['History', 'Math', 'Physics', 'CompSci']

print(courses[0:2]) # ['History', 'Math']

print(courses[2:]) # Not [2:0] ['Physics', 'CompSci']

print(courses[2:0]) # []


courses = ['History', 'Math', 'Physics', 'CompSci']


#Adding and substracting with methods uses parenthesis instead of square brackets

courses.append('Art')

print(courses) #['History', 'Math', 'Physics', 'CompSci', 'Art']

courses.insert(0, 'Art') 
print(courses) #['Art','History', 'Math', 'Physics', 'CompSci']

# Insert

courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Art', 'Educatiion']

courses.insert(0, courses_2)

print(courses[0]) # ['Art', 'Educatiion']
print(courses) # [['Art', 'Educatiion'], 'History', 'Math', 'Physics', 'CompSci']



 # "extend" method:

courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Art', 'Educatiion']

#courses.append(courses_2) # ['History', 'Math', 'Physics', 'CompSci', ['Art', 'Educatiion']]

courses.extend(courses_2) # ['History', 'Math', 'Physics', 'CompSci', 'Art', 'Educatiion']

print(courses)# ['History', 'Math', 'Physics', 'CompSci', ['Art', 'Educatiion'], 'Art', 'Educatiion']


courses = ['History', 'Math', 'Physics', 'CompSci']

print(courses) #['History', 'Math', 'Physics', 'CompSci']


courses = ['History', 'Math', 'Physics', 'CompSci']
  
courses.remove('Math')

print(courses) #['History', 'Physics', 'CompSci']
  
courses.pop()# pops out the last element of the list

print(courses)#['History', 'Physics']

popped = courses.pop()

print(courses) #['History']
print(popped) #Physics

#Sort:

courses = ['History', 'Math', 'Physics', 'Compsci']
courses.reverse()
print(courses)# ['Compsci', 'Physics', 'Math', 'History']



courses = ['History', 'Math', 'Physics', 'CompSci']
nums = [1, 5, 2, 4, 3]


courses.sort()
nums.sort()
courses.reverse()


print(courses) #['CompSci', 'History', 'Math', 'Physics']
print(nums) #[1, 2, 3, 4, 5] 

courses = ['History', 'Math', 'Physics', 'CompSci']

courses.reverse()
print(courses) # ['CompSci', 'Physics', 'Math', 'History']

Non





 # An easy way to order in reverse order instead of: courses.reverse()

courses = ['History', 'Math', 'Physics', 'CompSci']
nums = [1, 5, 2, 4, 3]

courses.sort(reverse=True)
nums.sort(reverse=True)

print(courses) #['Physics', 'Math', 'History', 'CompSci']
print(nums) #[5, 4, 3, 2, 1] 


 # A sorted version of our list without altering the original list
# This is using the sorted function instead of the sorting method


courses = ['History', 'Math', 'Physics', 'CompSci']

sorted(courses)
print(courses) #['History', 'Math', 'Physics', 'CompSci']

sorted_courses = sorted(courses) # So you do not alter the original

print(sorted_courses) #['CompSci', 'History', 'Math', 'Physics'] 


 # More useful built-ins : min. max, sum

nums = [1, 5, 2, 4, 3]

print(min(nums)) #1

print(max(nums)) #5

print(sum(nums)) #15

 # To find the index of certain value we can use the index method

courses = ['History', 'Math', 'Physics', 'CompSci']

print(courses.index('CompSci')) #3 Note: first  time using a method inside of the print function, the other methods showed none
print(courses.index('Art')) # Value error: 'Art' is not in list




 # To check if our value is on our list we use the "in" operator to return a True or False result
courses = ['History', 'Math', 'Physics', 'CompSci']

print('Art' in courses) # False

 
print('Math' in courses) # True 

 # Also to look for values we use for loops


courses = ['History', 'Math', 'Physics', 'CompSci']

for item in courses:
    print(item) 
#History
#Math
#Physics
#CompSci









# my practice

sorted_courses = sorted(courses) # So you do not alter the original

print(sorted_courses) #['CompSci', 'History', 'Math', 'Physics']

# copy the result from terminal and define a variable 

qqq = ['CompSci', 'History', 'Math', 'Physics'] 

for item in qqq:
    print(item) #
#CompSci
#History
#Math   
#Physics 








 # To have the index and the value we want by using the "enumerate" function

courses = ['History', 'Math', 'Physics', 'CompSci']

for item in enumerate(courses):
    print(item )
(0, 'History')
(1, 'Math')   
(2, 'Physics')
(3, 'CompSci') 

 # Or:

courses = ['History', 'Math', 'Physics', 'CompSci']

for course in enumerate(courses):
    print(course)# 
(0, 'History')
(1, 'Math')   
(2, 'Physics')
(3, 'CompSci') 

 # And also:
courses = ['History', 'Math', 'Physics', 'CompSci']

for index, course in enumerate(courses):                                                                                                                                                 
    print(index, course)
#0 History
#1 Math   
#2 Physics
#3 CompSci 


# And if you want to start at a different value  uses start as a second parameter:


for index, course in enumerate(courses, start=1):
    print(index, course)

#1 History
#2 Math   
#3 Physics
#4 CompSci 

 #  Turn our list into strings separated by a certain value
# We use a string method called "joint" to pass in our list as a argument

courses = ['History', 'Math', 'Physics', 'CompSci']

#course_str = ', '.join(courses)

#print(course_str) # History, Math, Physics, CompSci

# Or:
  
courses = ['History', 'Math', 'Physics', 'CompSci']

course_str = '- '.join(courses)

#print(course_str) # History - Math - Physics - CompSci



new_list = course_str.split(' - ')

print(course_str) # History- Math- Physics- CompSci
print(new_list) # ['History- Math- Physics- CompSci']

  #  Turn our list into strings separated by a certain value
# We use a string method called "joint" to pass in our list as a argument
  
courses = ['History', 'Math', 'Physics', 'CompSci']

course_str = ' - '.join(courses)

#print(course_str) # History - Math - Physics - CompSci

#------------- To turn  back a string back into list----------

courses = ['History', 'Math', 'Physics', 'CompSci']

new_list = course_str.split(' - ')

print(course_str) # History- Math- Physics- CompSci
print(new_list) # ['History', 'Math', 'Physics', 'CompSci'] 


######################------------ Tuples ans Sets--------------################


# Mutable |\\\\///
list_1 = ['History', 'Math', 'Physics', 'Compsci']
list_2 = list_1

print(list_1)#['History', 'Math', 'Physics', 'Compsci']
print(list_2)#['History', 'Math', 'Physics', 'Compsci']

list_1[0] = 'Art'

print(list_1)# ['Art', 'Math', 'Physics', 'Compsci']
print(list_2)# ['Art', 'Math', 'Physics', 'Compsci']


# Immutable = use it if you know that values are not going to change

tuple_1 = ('History', 'Math', 'Physics', 'Compsci')
tuple_2 = tuple_1

print(tuple_1)# ['History', 'Math', 'Physics', 'Compsci']

print(tuple_2)#['History', 'Math', 'Physics', 'Compsci']


tuple_1[0] = 'Art'


# print(tuple_1)# TypeError: 'tuple' object does not support item assignment

# print(tuple_2)# TypeError: 'tuple' object does not support item assignment '''


# # Sets : values that have 'no' order and 'not' duplicates
# cs_courses = {'History', 'Math', 'Physics', 'CompSci'}

# print(cs_courses ) # {'CompSci', 'History', 'Physics', 'Math'}
# # {'History', 'Math', 'CompSci', 'Physics'}
# # {'Math', 'History', 'Physics', 'CompSci'}
# # {'Math', 'History', 'CompSci', 'Physics'}
# # {'Physics', 'Math', 'History', 'CompSci'}

# # sets are used to check if a value is part of a set
# # Sets throws away duplicates

# cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
# print(cs_courses )#{'Math', 'Physics', 'History', 'CompSci'}

# # When sets are used to check if a value is part of a set is called membership test
# # doing this more efficiently than lists

# cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}

# print('Math' in cs_courses ) # True

# # Sets are used to determine what values they either share or not share
# # what values of the sets have in common, use a 'intesrsection'

# cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
# art_courses = {'History', 'Math', 'Art', 'Design'  }


# print(cs_courses.intersection(art_courses)) # {'Math', 'History'}

# # Now to see what courses are in one dataset but not in the other one 
# cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
# art_courses = {'History', 'Math', 'Art', 'Design'  }

# print(cs_courses.difference(art_courses)) #  {'Physics', 'CompSci'} are not in the Art courses

# # To combine datasets and print all the elements use the union method

# cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
# art_courses = {'History', 'Math', 'Art', 'Design'  }

# print(cs_courses.union(art_courses))# {'History', 'Art', 'Physics', 'CompSci', 'Design', 'Math'}



# # How to create 'empty' lists, tuples and sets:

# # Empty lists
# empty_list = []
# empty_list = list() #Built-in list class

# # Empty Tuples
# empty_tuple = ()
# empty_tuple = tuple() #Built-in tuple class

# # Empty Sets
# empty_set = {} ##### This isn't right! It's a dictionary, not an empty set
# empty_set = set() # Built-in set class, yes use this!







#print(dir(courses)) # this is for info about the variable:
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__',
#  '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__',
#  '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__',
#  '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__',
#  '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index',
#  'insert', 'pop', 'remove', 'reverse', 'sort']



# courses = ['History', 'Math', 'Physics', 'CompSci']

# print(dir( courses)) #here2'''

'''courses = ['History', 'Math', 'Physics', 'CompSci']

#course_str = ', '.join(courses)

#print(course_str) # History, Math, Physics, CompSci


# Or:

 #  Turn our list into strings separated by a certain value
# We use a string method called "joint" to pass in our list as a argument
  
courses = ['History', 'Math', 'Physics', 'CompSci']

course_str = ' - '.join(courses)

#print(course_str) # History - Math - Physics - CompSci

#------------- To turn  back a string back into list----------

new_list = course_str.split(' - ')

print(course_str) # History- Math- Physics- CompSci
print(new_list) # ['History', 'Math', 'Physics', 'CompSci'] 

print(help(str.join))
Help on method_descriptor:

join(self, iterable, /)
    Concatenate any number of strings.
    
    The string whose method is called is inserted in between each given string.
    The result is returned as a new string.
    
    Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs' . '''



#print(help(str.split)) #yes
#print(help(list.split)) #no

#print(help(list.join)) # list has no attribute join'''



# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__',
#  '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__',
#  '__iter__', '__le__', 
#'__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__',
#'__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove',
#'reverse', 'sort']

'''
print(help(list))
# Help on class list in module builtins:

class list(object)
 |  list(iterable=(), /)
 |
 |  Built-in mutable sequence.
 |
 |  If no argument is given, the constructor creates a new empty list.
 |  The argument must be an iterable if specified.
 |
 |  Methods defined here:
 |
 |  __add__(self, value, /)
 |      Return self+value.
 |
 |  __contains__(self, key, /)
 |      Return key in self.
 |
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |
 |  __eq__(self, value, /)
 |      Return self==value.
 |
 |  __ge__(self, value, /)
 |      Return self>=value.
 |
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |
 |  __gt__(self, value, /)
 |      Return self>value.
 |
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |
 |  __imul__(self, value, /)
 |      Implement self*=value.
 |
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  __iter__(self, /)
 |      Implement iter(self).
 |
 |  __le__(self, value, /)
 |      Return self<=value.
 |
 |  __len__(self, /)
 |      Return len(self).
 |
 |  __lt__(self, value, /)
 |      Return self<value.
 |
 |  __mul__(self, value, /)
 |      Return self*value.
 |
 |  __ne__(self, value, /)
 |      Return self!=value.
 |
 |  __repr__(self, /)
 |      Return repr(self).
 |
 |  __reversed__(self, /)
 |      Return a reverse iterator over the list.
 |
 |  __rmul__(self, value, /)
 |      Return value*self.
 |
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |
 |  __sizeof__(self, /)
 |      Return the size of the list in memory, in bytes.
 |
 |  append(self, object, /)
 |      Append object to the end of the list.
 |
 |  clear(self, /)
 |      Remove all items from list.
 |
 |  copy(self, /)
 |      Return a shallow copy of the list.
 |
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |
 |  extend(self, iterable, /)
 |      Extend list by appending elements from the iterable.
 |
 |  index(self, value, start=0, stop=9223372036854775807, /)
 |      Return first index of value.
 |
 |      Raises ValueError if the value is not present.
 |
 |  insert(self, index, object, /)
 |      Insert object before index.
 |
 |  pop(self, index=-1, /)
 |      Remove and return item at index (default last).
 |
 |      Raises IndexError if list is empty or index is out of range.
 |
 |  remove(self, value, /)
 |      Remove first occurrence of value.
 |
 |      Raises ValueError if the value is not present.
 |
 |  reverse(self, /)
 |      Reverse *IN PLACE*.
 |
 |  sort(self, /, *, key=None, reverse=False)
 |      Sort the list in ascending order and return None.
 |
 |      The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
 |      order of two equal elements is maintained).
 |
 |      If a key function is given, apply it once to each list item and sort them,
 |      ascending or descending, according to their function values.
 |
 |      The reverse flag can be set to sort in descending order.
 |
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |
 |  __class_getitem__(...) from builtins.type
 |      See PEP 585
 |
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |
 |  __hash__ = None

None '''

#print(help(list.sort)) # Help on method_descriptor:

'''sort(self, /, *, key=None, reverse=False)
    Sort the list in ascending order and return None.

    The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
    order of two equal elements is maintained).

    If a key function is given, apply it once to each list item and sort them,
    ascending or descending, according to their function values.

    The reverse flag can be set to sort in descending order.

None'''

# Mutable
# list_1 = ['History', 'Math', 'Physics', 'Compsci']
# list_2 = list_1

# print(list_1)#['History', 'Math', 'Physics', 'Compsci']
# print(list_2)#['History', 'Math', 'Physics', 'Compsci']

# list_1[0] = 'Art'

# print(list_1)# ['Art', 'Math', 'Physics', 'Compsci']
# print(list_2)# ['Art', 'Math', 'Physics', 'Compsci']

# Immutable = use it if you know that values are not going to change
# tuple_1 = ('History', 'Math', 'Physics', 'Compsci')
# tuple_2 = tuple_1

# print(tuple_1)# ['History', 'Math', 'Physics', 'Compsci']

# print(tuple_2)#['History', 'Math', 'Physics', 'Compsci']


# tuple_1[0] = 'Art'

# print(tuple_1)# TypeError: 'tuple' object does not support item assignment

# print(tuple_2)# TypeError: 'tuple' object does not support item assignment


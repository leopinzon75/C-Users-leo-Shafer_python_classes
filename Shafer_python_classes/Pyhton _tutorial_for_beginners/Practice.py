'''courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Art', 'Educatiion']

courses.insert(0, courses_2)

print(courses[0]) # ['Art', 'Educatiion']
print(courses) # [['Art', 'Educatiion'], 'History', 'Math', 'Physics', 'CompSci']'''

'''# "extend" method:

courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Art', 'Educatiion']

#courses.append(courses_2) # ['History', 'Math', 'Physics', 'CompSci', ['Art', 'Educatiion']]
courses.extend(courses_2) # ['History', 'Math', 'Physics', 'CompSci', 'Art', 'Educatiion']
print(courses)# ['History', 'Math', 'Physics', 'CompSci', ['Art', 'Educatiion'], 'Art', 'Educatiion']


print(help(dir))

Help on built-in function dir in module builtins:

dir(...)
    dir([object]) -> list of strings
    
    If called without an argument, return the names in the current scope.
    Else, return an alphabetized list of names comprising (some of) the attributes
    of the given object, and of attributes reachable from it.
    the default dir() logic is used and returns:
      for a module object: the module's attributes.
      for a class object:  its attributes, and recursively the attributes
        of its bases.
      for any other object: its attributes, its class's attributes, and
        recursively the attributes of its class's base classes.

None
 
courses = ['History', 'Math', 'Physics', 'CompSci']

courses.reverse()
print(courses) # ['CompSci', 'Physics', 'Math', 'History']

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
print(cs_courses ) #{'CompSci', 'History', 'Physics', 'Math'}

{'History', 'Math', 'CompSci', 'Physics'}
{'Math', 'History', 'Physics', 'CompSci'}
{'Math', 'History', 'CompSci', 'Physics'}
{'Physics', 'Math', 'History', 'CompSci'} 

cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
print(cs_courses )#{'Math', 'Physics', 'History', 'CompSci'} 
 

cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}

print('Math' in cs_courses ) # True  


# Sets are used to determine what values they either share or not share
# what values of the sets have in common, use a 'intesrsection'

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'  }

print(cs_courses.intersection(art_courses)) # {'Math', 'History'} 


# Now to see what courses are in one dataset buut not in the other one 
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'  }

print(cs_courses.difference(art_courses)) # {'Physics', 'CompSci'} 

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'  }

print(cs_courses.union(art_courses))# {'History', 'Art', 'Physics', 'CompSci', 'Design', 'Math'}'''


courses = ['History', 'Math', 'Physics', 'Compsci']
courses.reverse()
print(courses)


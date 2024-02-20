
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

#-- All of the keys are strings in the example but
#they can be any immuatble datatype

# print(student) #{'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

# print(student['name'])# John

# print(student['courses'])# ['Math', 'CompSci']

# student = { 1: 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

# print(student[1]) # John

# Try to access a key that does not exist:

#print(student['phone']) # error: key error "phone"


#--- We can return none or a default value in a key value using get method even if the key is not in the dictionary

# print(student.get('phone'))#None
  
  
# print(student.get('phone', 'Not Found'))#Not Found     

# -- How to 'add' a new enter to the dictionary: note the use of square brackets

# student['phone'] = '555-5555' 

# print(student.get('phone', 'Not Found'))# 555-5555   



#-- How to update a key value: square brackets also

# print(student)student = { 'name' : 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

# student['name'] = 'Jane'  

# print(student)# {'name': 'Jane', 'age': 25, 'courses': ['Math', 'CompSci']}


#-- To update multiple values at the time we can use the 'update' method


# student = { 'name' : 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

# student.update({'name' : 'Jane', 'age' :26, 'phone' : '555-5555'}

# print(student)# {'name': 'Jane', 'age': 26, 'courses': ['Math', 'CompSci'], 'phone': '555-5555'}


#-- To delete a specific key and its value


# student = { 'name' : 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

# del student['age']

# print(student)# {'name': 'John', 'courses': ['Math', 'CompSci']}



#-- We can also delete a specific key and its value and 
# call its value with the 'pop' method



# student = { 'name' : 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

# age = student.pop('age')

# print(student)# {'name': 'John', 'courses': ['Math', 'CompSci']}

# print(age)# 25



#-- How can we 'loop' through all the keys and values of our dictionary


# student = { 'name' : 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

# print(len(student))# 3

# print(student.keys())# dict_keys(['name', 'age', 'courses'])

#print(student.values())# dict_values(['John', 25, ['Math', 'CompSci']])

#print(student.items())# dict_items([('name', 'John'), ('age', 25), ('courses', ['Math', 'CompSci'])])

# student = { 'name' : 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

# for key in student:
#     print(key)
#name
#age
#courses
    
# To loop through key and values we need the 'items' method

for key, value in student.items():
    print(key, value) 

#name John
#age 25
#courses ['Math', 'CompSci']
    
 C:\Users\leo\Shafer_python_classes_and_methods_tutorial\Pyhton _tutorial_for_beginners\Dictionaries_Working_with_value_pairs_6C:\Users\leo\Shafer_python_classes_and_methods_tutorial\Pyhton _tutorial_for_beginners\Dictionaries_Working_with_value_pairs_6












# for key, value in student.items():
#     print(key, value)



































#print(help(mutable))

#print(help(dict.items)) # Help on method_descriptor:






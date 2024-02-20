 
# For loops iterates through certain number of values
# But While loops will just keep going until a certain condition is met

#For loops

# nums = [1,2,3,4,5] 

# for num in nums:
#     print(nums)   

#1
#2
#3    
#4
#5 

# Important keywords in loops: "break and continue" will stop and will make the loop go on
# break statement
    

# nums = [1,2,3,4,5]    
# for a in nums:
     
#     if a == 3:
#         print('Found!')# 12Found!
#         break
#     print(a)
# #1
# #2
# #Found!

# nums = [1,2,3,4,5]
# for a in nums:
    
#     print(a)
#     if a == 3:
#         print('Found!')# 11223Found!
#         break
#     print(a) 

#1
#1
#2
#2    
#3
#Found!

# continue statement

# nums = [1,2,3,4,5,]

# for num in nums:
#     if num == 3:
#         print('Found!')# 12Found!45
#         continue
#     print(num)

#1
#2
#Found!
#4
#5



# # Nested loops, inner loops

# nums = [1,2,3,4,5,]   
# for num in nums:
#     for letter in 'abc':
#            print(num, letter)
    
# 1 a
# 1 b
# 1 c
# 2 a
# 2 b
# 2 c
# 3 a
# 3 b
# 3 c
# 4 a
# 4 b
# 4 c
# 5 a
# 5 b
# 5 c
 

# for num in nums:
#     for letter in 'abc':
#          print(letter, num)
#        

# a 1
# b 1
# c 1
# a 2
# b 2
# c 2
# a 3
# b 3
# c 3
# a 4
# b 4
# c 4
# a 5
# b 5
# c 5



 


# To run through a loop a certain numbers of times we can use the 'range' function
# # includes 10 numbers including 0 and goes up but not including 10


# for i in range(10):
#     print(i)

# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9 



# for i in range(1, 11):
#     print(i)

# 1
# 2 
# 3 
# 4 
# 5 
# 6 
# 7 
# 8 
# 9 
# 10


# Again: For loops iterates through certain number of values
# But While loops will just keep going until a certain condition is met

#While loops
# x = 0

# while x < 10:
#     print(x)
#     x += 1

# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
 

# To break out of the while loop
    
 
# x = 0

# while x < 10:
#     if x == 5:
#         break
#     print(x)
#     x +=  1
    
# 0
# 1
# 2
# 3
# 4

# To create an infinite loop replace the comparison with the value of True
# We use the coonditional to break out
# Without the conditional runs constantly, non stop

# x = 0

# while True:
#     if x == 5:
#         break
#     print(x)
#     x +=  1

# 0
# 1
# 2
# 3
# 4
 
# x = 0

# while True:
#     print(x)
#     x +=  1


# 29 778
# 30000 operations per every 10 sec
# 3000 operations per sec



# 15 sec:
# mine =   44 132
# his = 2 124 686
#4 times faster
    #'''#click on terminal and press control c.'''







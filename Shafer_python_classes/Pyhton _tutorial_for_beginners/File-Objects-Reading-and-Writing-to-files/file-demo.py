# File Objects

f = open('test.txt', 'r')

print(f.name)#test.txt

print(f.mode)#r

# print(f.read())#

f.close()

# Contex manager to close automatically, it let us work
# with the file within this block of code and will close the file also in case of errors
#

with open('test.txt', 'r') as f:
    pass

print(f.closed)#True

# print(f.read())#ValueError: I/O operation on closed file.


#Let's use the context manager from now on

# with open('test.txt', 'r') as f:
#     f_contents = f.read()
#     print(f_contents)#

# 1) This is a test file
# 2) With multiple lines of data...
# 3) Third line
# 4) Fourth line
# 5) Fifth line
# 6) Sixth line
# 7) Seventh line
# 8) Eighth line
# 9) Ninth line
# 10) Tenth line
    
# Other methods on reading the files, readlines:

# with open('test.txt', 'r') as f:
#     f_contents = f.readlines()
#     print(f_contents)

#['1) This is a test file\n', '2) With multiple lines of data...\n',
#'3) Third line\n', '4) Fourth line\n', '5) Fifth line\n', '6) Sixth line\n',
#'7) Seventh line\n', '8) Eighth line\n', '9) Ninth line\n', '10) Tenth line']
    
# with open('test.txt', 'r') as f:
#     f_contents = f.readline()
#     print(f_contents)
# #1) This is a test file
#     f_contents = f.readline()
#     print(f_contents)
# #2) With multiple lines of data...
    
#To avoid an extra line in the
#command line passing an empty string at the end of the print statement
# with open('test.txt', 'r') as f:
#     f_contents = f.readline()
#     print(f_contents, end="")
# #1) This is a test file
#     f_contents = f.readline()
#     print(f_contents, end="")

# If we run the entire file all at once, a large file, we can run out of memory,
# insted we can iterate with a loop which avoid the reading all at once

# with open('test.txt', 'r') as f:

#     for line in f:
#         print(line, end='')

# If you need more control over your file we can use f.read and specify the amount

# with open('test.txt', 'r') as f:

#     f_contents = f.read(100)
#     print(f_contents, end="")

# 1) This is a test file
# 2) With multiple lines of data...
# 3) Third line
# 4) Fourth line
# 5) Fifth line


# And if you repeat it again will print the next part until returns an
#empty string "not visible" but you need to learn this

# with open('test.txt', 'r') as f:

#     f_contents = f.read(100)
#     print(f_contents, end="")

#     f_contents = f.read(100)
#     print(f_contents, end="")

#     f_contents = f.read(100)
#     print(f_contents, end="")


# 1) This is a test file
# 2) With multiple lines of data...
# 3) Third line
# 4) Fourth line
# 5) Fifth line
# 6) Sixth line
# 7) Seventh line
# 8) Eighth line
# 9) Ninth line
# 10) Tenth line

# for a large file we still need to iterate over chunks if it.
# we use f.read use a variable instead of the number
    
# with open('test.txt', 'r') as f:

#     size_to_read = 100

#     f_contents = f.read(size_to_read)

#     while len(f_contents) >0:
#         print(f_contents, end="")# do not run it yet, needs the copy of the  code to stop the loop
#         f_contents = f.read(size_to_read)




#********************************** Necesary to practice!!!!!!!!!!!!!!!!!

# # To get a better idea lets change the amount to 10 and add an asterisk for every loop

# with open('test.txt', 'r') as f:

#     size_to_read = 10

#     f_contents = f.read(size_to_read)

#     while len(f_contents) > 0:
#         print(f_contents, end="*")# do not run it yet, needs the copy of the  code to stop the loop
#         f_contents = f.read(size_to_read)
# 1) This is* a test fi*le
# 2) With* multiple *lines of d*ata...
# 3) *Third line*
# 4) Fourth* line
# 5) F*ifth line
# *6) Sixth l*ine
# 7) Sev*enth line
# *8) Eighth *line
# 9) Ni*nth line
# 1*0) Tenth l*ine*   
        #

#this is a personal excercise, just erasing the asterix and the end keyword on the printing statement

# with open('test.txt', 'r') as f:

#     size_to_read = 10

#     f_contents = f.read(size_to_read)

#     while len(f_contents) > 0:
#         print(f_contents)# do not run it yet, needs the copy of the  code to stop the loop
#         f_contents = f.read(size_to_read)
# 1) This is
#  a test fi
# le
# 2) With
#  multiple
# lines of d
# ata...
# 3)
# Third line

# 4) Fourth
#  line
# 5) F
# ifth line

# 6) Sixth l
# ine
# 7) Sev
# enth line

# 8) Eighth
# line
# 9) Ni
# nth line
# 1
# 0) Tenth l
# ine

# To see the position of the advance use file tell()
        
# with open('test.txt', 'r') as f:

#     size_to_read = 10

#     f_contents = f.read(size_to_read)

#     print(f.tell())

#We can manipulate the current position using the seek method
    
# with open('test.txt', 'r') as f:

#     size_to_read = 10

#     f_contents = f.read(size_to_read)
#     print(f_contents, end='')

#     f_contents = f.read(size_to_read)
#     print(f_contents)
#outpput  1) This is a test fi:
    
# Here we use seek:
# with open('test.txt', 'r') as f:

#     size_to_read = 10

#     f_contents = f.read(size_to_read)
#     print(f_contents, end='')

#     f.seek(0)
    

#     f_contents = f.read(size_to_read)
#     print(f_contents)
   
#1) This is1) This is





# Let's write now into the files!
# If open is in r mode, the write function will throw an error

    
# with open('test.txt', 'r') as f:
#     f.write('Test')# io.UnsupportedOperation: not writable


# When we use 'w' mode the file gets created, if it exist will over write on it, becareful



# with open('test2.txt', 'w') as f:
#     pass# At this moment the file gets created at the explorer

# Now we can write on this new file

# with open('test2.txt', 'w') as f:
#     f.write('Test')# click in test2 file and the word Test has been written 



# Let's write the same twice

# with open('test2.txt', 'w') as f:
#     f.write('Test')
#     f.write('Test')# on test2 = TestTest


# can use seek() when writing files to set the position back to the beginning of the file
# but works differently than when working with reading files


# with open('test2.txt', 'w') as f:
#     f.write('Test')
#     f.seek(0)
#     f.write('Test')# on test2  = goes back to one 'Test'
    
#

# with open('test2.txt', 'w') as f:
#     f.write('Test')
#     f.seek(0)
#     f.write('R')# on test2  = Rest

  


# Let's use read and write to use multiple files at the same time
    
# with open('test.txt', 'r') as rf:
#     with open('test_copy.txt', 'w') as wf:
#         for line in rf:
#             wf.write(line)# when you run the code it creates the file copied with characters

# To use almost the same commands but for coping images: need to type b for binary after the mode, r, or w.
            
# with open('puppy.jpeg', 'rb') as rf:
#     with open('puppy_copy.jpeg', 'wb') as wf:
#         for line in rf:
#             wf.write(line)# when you run the code it creates the file copied with byte images  

# To copy controlling the chunk size:
            
# with open('puppy.jpeg', 'rb') as rf:
#     with open('puppy_copy.jpeg', 'wb') as wf:
#         chunk_size = 4096 
#         rf_chunk = rf.read(chunk_size)
#         while len(rf_chunk) > 0:
#             wf.write(rf_chunk)
#             rf_chunk = rf.read(chunk_size)      


# when you run the code it creates the file copied with byte images                 
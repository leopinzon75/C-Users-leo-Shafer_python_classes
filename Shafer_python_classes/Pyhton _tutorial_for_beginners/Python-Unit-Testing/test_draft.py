import unittest
import calc



# On the terminal go to the file location then run this command: 
# python test_draft.py and then this command:python  -m unittest test_draft.py


# class TestCalc(unittest.TestCase):

#     def  test_add(self):
#          result = calc.add(10, 5) #check again importing modules chapter to review this feature
#          self.assertEqual(result, 15)

# Output from the terminal:
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.001s

# OK





# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s

# OK
      


# You have to name the file and the defs with the word test at the beginning or
# the test will count 0

# class TestCalc(unittest.TestCase):

#     def _add_test(self):
#         result = calc.add(10, 5)
#         self.assertEqual(result, 15)


# Output:Ran 0 tests in 0.000s

#OK     

# What happen if we set the test with a wrong calculation  
class TestCalc(unittest.TestCase):

    def  test_add(self):
         result = calc.add(10, 5) #check again importing modules chapter to review this feature
         self.assertEqual(result, 14)

# Output:
# F
# ======================================================================
# FAIL: test_add (__main__.TestCalc)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "c:\Users\leo\Shafer_python_classes\Pyhton _tutorial_for_beginners\Python-Unit-Testing
# \test_draft.py", line 54, in test_add
         
#  self.assertEqual(result, 14)
# AssertionError: 15 != 14

# ----------------------------------------------------------------------
# Ran 1 test in 0.059s

# FAILED (failures=1)

# Now, instead of setting the result variable and testing that,lets drop the function directly into the assert 
# equal statement coping this and replacing the result variable actually with our add function
#
class TestCalc(unittest.TestCase):

    def  test_add(self):
          #check again importing modules chapter to review this feature
         self.assertEqual( calc.add(10, 5), 15)


# And now check some edge cases:
class TestCalc(unittest.TestCase):

    def  test_add(self):
          #check again importing modules chapter to review this feature
         self.assertEqual( calc.add(10, 5), 15)
         self.assertEqual( calc.add(-1, 1), 0)
         self.assertEqual( calc.add(-1, -1), -2)

# Output:
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s

# OK






# # Then add on the file dunder method to now run it on the editor
if __name__ == '__main__':
    unittest.main()
# Script Location  # how to fined the files location
'''
- os.path.dirname(os.path.abspath(__file__)): Get the directory where the Python script is located.
- __file__: Represents the relative path of the currently executing script. Use it with os.path functions to get the script's location.
'''

from os import *

d = "4Raisan/Python-libraries-/1. _OS_library_in_py_.py" 
# or use __file__ for use the script what we ran
op = path.dirname(path.abspath(__file__))
op2 = path.dirname(path.abspath(d))

print(op)
print()
print(op2)
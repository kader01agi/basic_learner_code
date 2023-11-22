#(https://www.w3schools.com/python/python_math.asp)
#(https://www.w3schools.com/python/module_math.asp)

print(9 % 4)

import math

print(math.fmod(9, 4))
print(math.remainder(9, 4))
# fmod() rounds towards zero, while remainder() rounds towards the nearest integer.
print(math.fmod(-9, 4))  
print(math.remainder(-9, 4))

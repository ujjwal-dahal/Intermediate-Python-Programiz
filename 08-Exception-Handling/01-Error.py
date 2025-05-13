
'''
Types of Error
1. Syntax Error
-> these error are due to improper use of Python syntax , such as missing parenthesis , wrong indentation , missing colons , etc

Example:

if 5 > 3
  print("5 is greater than 3)



2. Exceptions
 Even if our code is syntactically correct, we may sometimes get an error. For example, if we divide a number by 0, we get an error.
 
 
#Different Types of Exceptions

Let's see a few different types of exceptions.

1. IndexError Exception

-> This exception occurs when the index we are using in a sequence (list, tuple, string, etc.) is out of range. 

For example,

numbers = [2, 8, 5]
print(numbers[4])   # raises IndexError Exception
Here, the numbers list has three items. So we can use 0, 1 or 2 as an index. However, in our program we are using 4 as an index.


2. KeyError Exception

-> This exception occurs when a key is not found in a dictionary. For example,

person = {'name': 'Struat', 'age': 30}
# raises KeyError Exception
print(person['profession']) 
The person dictionary doesn't have profession as a key.

3. ValueError Exception

-> This exception occurs if a function or an operation is applied to an incorrect type. For example,

import math

# raises TypeError Exception
result = math.sqrt('Hello')
print(result)
math.sqrt() cannot take a string as an argument.

 

'''
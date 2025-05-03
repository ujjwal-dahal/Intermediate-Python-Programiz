""" 
-> Recursion means Function le afailai Call garnu until base condition meet huncha

Two Parts:

Base Part : Jasle Recursive Function lai Stop i.e Terminate garcha
Recursive Part : Jun chai Recursive Function ko Sub part ho jun Function le afailai call garcha

A function that calls itself is known as a recursive function. And, this process is known as recursion.

"""


#Factorial 


def factorial_calculation(n):
  if n==0 | n==1:
    return 1
  
  else:
    return n * factorial_calculation(n-1)
  
print(f"Factorial of 5 is {factorial_calculation(5)}")
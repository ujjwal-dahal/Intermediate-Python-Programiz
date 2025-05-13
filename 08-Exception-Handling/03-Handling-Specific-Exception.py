
#Handling Specific Exception


'''
It's also possible to handle different types of exceptions in different ways. For example,

If the ZeroDivisionError exception is raised, we can run one set of code.
If the IndexError exception is raised, we can run another set of code.
'''


try:
  numerator = int(input("Numerator : "))
  denominator = int(input("Denominator : "))
  result = numerator / denominator
  
  print(result)
  
  myList = [1,2,3,4]
  index = int(input("Enter Index : "))
  print(myList[index])
  
except ZeroDivisionError:
  print("Denominator cannot be 0")
  
except IndexError:
  print("Index is wrong")
  
  #-> Eddi 1st ko le exception show garo bhane i.e result ma exception aaucha ZeroDivisionError jasle gaarda tesko except ko code execute huncha 
  
  #-> Suru ma jun ko exception aaucha tesko block ko code run huncha tyo dekhi tala ko execute hudaina

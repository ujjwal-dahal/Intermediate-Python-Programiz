
'''
-> Exception bhaneko Syntatically correct bhaye pani Program execute bhayeko bela aaune Error ho

-> So Most of the time, rather than showing this default error message, we may want to show a custom message that's more helpful or run a different set of code. This is known as exception handling.

-> we use 'try...except' block to handle exception
'''



# try:
#   numerator = int(input("Enter Denominator : "))
#   denominator = int(input("Enter Denominator : "))
  
#   result = numerator /denominator
#   print(result)

# except:
#   print("Denomintor cannot be 0")
  
'''
-> Jaba denominator 0 hudaina Taba exception create hudaina so exception block is skipped

-> But when denominator = 0 then
result = numerator / denominator huda 
exception create huncha so teti bela 
result below ko code skipped huncha
sidai except block run huncha
'''

#Program 1

# try:
#   numbers = [10,20,30]
#   index = int(input("Enter Number : "))
#   print(numbers[index])
# except:
#   print("Index is wrong")

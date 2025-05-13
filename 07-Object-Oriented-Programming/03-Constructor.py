
'''
-> Variable i.e Attributes define garnu cha bhane Constructor use garincha

-> Constructor banauna Function name "__init__" use huncha

-> Constructor ko Main Feature bhaneko 
Jaba hamile Object banauchau taba Constructor Function Call huncha

-> When this object is created, the __init__() method is automatically called. Inside this method,

self takes the value of object student1

'''


class Student:
  def __init__(self , name,age):
    self.name = name
    self.age = age 
  
  def displayData(self):
    print(f"Student Name : {self.name} Age : {self.age}")
    
userName = input("Name : ")
userAge = int(input("Age : "))

obj1 = Student(userName , userAge)

obj1.displayData();


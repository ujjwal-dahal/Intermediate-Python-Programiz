


class Person:
  def __init__(self , name , age):
    self.name = name
    self.age = age 
    
  def displayData(self , Person2):
    print(f"Main Object ko Value : {self.name} {self.age}")
    print(f"Argument Object ko Value : {Person2.name} {Person2.age}")
    

person1 = Person("Ujjwal",21) # Yo huda __init__(self , "Ujjwal", 21) Call huncha
#teti bela  "self" is person1 so person1.name = "Ujjwal" ani person1.age = 21 huncha

person2 = Person("Ram",35) # Yo huda __init(self , "Ram" , 35) Constructor Call huncha ani Yo person2 object ko name ra age variable ma value assign huncha using self le

person1.displayData(person2)
#Person2 = person2 object huncha
#so Person2.name is person2.name ho


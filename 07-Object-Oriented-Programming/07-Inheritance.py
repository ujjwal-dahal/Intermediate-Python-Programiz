
'''
-> Euta Class le arko Class ko Properties lai inherit garne Feature

-> Jun Class le inherit garcha tyo Class is Child Class or Derived Class
& Jasto Inherit garcha Tyo Class is Parent Class or Base Class

'''


#parent class

# class Animal:
#   def color_of_animal(self):
#     print("Color of Animal is : ")
    
# class Cat(Animal):
#   def meow(self):
#     print("Sound of Cat is Meow")
    
# class Dog(Animal):
#   def bark(self):
#     print("Sound of Dog is Bark")
    
# obj1 = Cat();
# obj1.meow()
# obj1.color_of_animal() #Child Class le Parent Class ko Inherit gareko 


# obj2 = Dog()
# obj2.bark()
# obj2.color_of_animal()


class Polygon:
  def __init__(self , sides):
    self.sides = sides 
    
  def display_info(self):
    print("This is Polygon")
    
  def get_perimeter(self):
    result = sum(self.sides)
    return result
    
class Triangle(Polygon):
  def display_info(self):
    print("Triangle is a Polygon having 3 Sides")
    
obj1 = Triangle([1,2,3])

perimeter = obj1.get_perimeter(); #Derived Class le Parent Class ko Function call gareko
print(f"Perimeter is {perimeter}")

obj1.display_info();

'''
Since Parent Class ra Child Class ma Same Named Method cha so hamile Class garda yaa Method Overriding huncha which means Derived Class ko Function le Base Class ko Function lai Override huncha so
Derived Class ko Function Call huncha
'''


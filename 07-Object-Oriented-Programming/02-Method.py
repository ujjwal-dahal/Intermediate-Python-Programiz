
'''
-> Class bhitra ko Function lai Method bhanincha

-> Method ma Always "self" Parameter huncha

-> Remember: We must always use "self" as the first argument in the function definition. 
This "self" takes the value of the object calling it.

'''


class Student:
  
  def Study(self , name , hour):
    self.name = name
    self.hour = hour 
    print(f"{self.name} Study for {self.hour}")
    

object1 = Student();


#dot operator is used to call method of class
object1.Study("Ujjwal",12)
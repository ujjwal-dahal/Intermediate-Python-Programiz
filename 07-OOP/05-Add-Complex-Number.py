
'''
complex number = real part + imaginary part * i

so coomplex number add huda real part + real part & imaginary part + imaginary part

'''


class ComplexNumber:
  
  def __init__(self , realPart , imagPart):
    self.realPart = realPart
    self.imagPart = imagPart
    
  def addNumber(self , Object):
    total_real_part = self.realPart + Object.realPart
    total_imag_part = self.imagPart + Object.imagPart
    print(f" {self.realPart}+{self.imagPart}i\n+{Object.realPart}+{Object.imagPart}i \n\n={total_real_part}+{total_imag_part}i")
    
    

complex1 = ComplexNumber(2,3)

complex2 = ComplexNumber(5,6)

complex1.addNumber(complex2)
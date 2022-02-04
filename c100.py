Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
class Robot():

  def __init__(self, name, CardNmuber, pin) :
      self.name = name
      self.Cardnumber = CardNmuber
      self.pin = pin


  def introduce_Name(self):
    print( "Hello" + self.name)
  
  def introduce_number(self):
    print( "Your Cardnumber is : " + self.Cardnumber)  
  
r1 = Robot("Harjot", "123456", "1234" )
print(r1.introduce_Name())
print(r1.introduce_number())
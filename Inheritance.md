Inheritance : LỚP KẾ THỪA trong lập trình hướng đối tượng : cho phép một lớp có thể kế thừa toàn bộ thuộc tính và phương thức từ 1 lớp khác
Lớp cha: lớp dc kế thừa, lớp nào cũng có thể là lớp cha
Lớp con: là lớp kế thừa từ lớp khác. Từ lớp con có thể phát triển thêm các thuộc tính hoặc phương thức mà lớp cha k có.
VÍ dụ:
Lớp cha:
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

x = Person("Anh", "Huy")
x.printname() ==> Anh Huy

Lớp con: 
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

x = Student("Anh", "Huy")
x.printname() ==> Anh Huy
Ví dụ:
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the actiup of", self.graduationyear)

x = Student("Anh", "Huy", 2025)
x.welcome(): Welcome Anh Huy to the acctiup of 2025
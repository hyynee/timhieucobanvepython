class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

x = Person("Anh", "Huy")
x.printname()

class Student(Person):
  pass
# sài pas khi k cần thêm thuộc tính hay phương thức nào khác

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

y = Student("Anh", "Huy")
y.printname()

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the actiup of", self.graduationyear)

z = Student("Anh", "Huy", 2025)
z.welcome()
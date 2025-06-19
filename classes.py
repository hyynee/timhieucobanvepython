from django.db import models


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    return f"Hello, my name is {self.name} and I am {self.age} years old."


    
x = Person(name="huy", age=21)
print(x.greet())  # Output: Hello, my name is huy and I am 21 years old.
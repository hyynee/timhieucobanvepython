from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return f"{self.name}({self.age})"
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
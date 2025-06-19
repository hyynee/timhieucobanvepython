# Class: dùng để tạo 1 lớp chứa các thuộc tính hoặc phương thức
ví dụ: class Person(models.Model):
       name = models.CharField(max_length=100)
       age = models.IntegerField()

       def __str__(self):
         return f"{self.name}({self.age})"

       def hello(seft):
         print("Hello my name is" + seft.name)
# có thể tạo dc 1 đối tượng từ lớp đó
p1 = Person("huy",21)
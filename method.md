Method: là các phương thức mà có thể sử dụng trên danh sách
ví dụ như insert(),coppy(),clear(),count(),remove(),sort()..

ví dụ code bên : method.py

method: phương thức của class (nhận đối tượng là object | instance làm đối số đầu tiên)

# Set và get : dùng để thay đổi hoặc lấy giá trị thuộc tính

# self: đại diện cho instance (đối tượng) của class : thao các với thuộc tính của đối tượng

class Person:
name = 'No name'
def setName(self,new_name):
self.name = new_name;
def getName(self):
return self.name
a=Person();
a.setName('Anh Huy')
print(a.getName())

# Class Method và Static Method

Class Method :
+phương thức nay nhận tham số đầu tiên là cls (thay vì self như các phương thức thông thường);
+cls: đại diện cho class, không phải instance. Nên có thẻe gọi phương thức này từ chính class hoặc từ instance của class

- thường sử dụng khi truy cập hoặc thay đổi thuộc tính của class, tạo ra đối tượng
- thường dc khai báo với decorator là: @classmethod
  ví dụ:
  class Employee:
  salary_up = 2;
  nums_of_oject = 0;
  def **init**(self, fname,lname, salary,age):
  self.fname = fname
  self.lname = lname
  self.salary = salary
  self.age = age
  Employee.nums_of_oject += 1

      def get_fullname(self):
          return self.fname + ' ' + self.lname
      def incre_salary(self):
          self.salary = self.salary * self.salary_up

      @classmethod
      def change_salary_up(cls, new_salary_up): (cls: ở đây dc hiểu là lớp Employee)
          cls.salary_up = new_salary_up
      @classmethod
      def create_employee(cls, fname, lname, salary, age):
          return cls(fname, lname, salary, age)

emp_1 = Employee('Anh', 'Huy', 50000, 30)
emp_2 = Employee('Nguyen', 'A', 60000, 25)

print(emp_1.salary_up);
print(emp_2.salary_up);
==> đều sẽ in ra dc là 2 vì biến salaryn_up đang là biến thuộc về class nên các đối tượng có thể truy cập vào
cls: lúc này đang là class Employee
Employee.change_salary_up(3)
print(emp_1.salary_up);
print(emp_2.salary_up);
==> kết quả lúc này in ra sẽ là 3,3
#emp_1 đang là đối tượng là class Employee nên vẫn truy cập và thay đổi giá trị dc
emp_1.change_salary_up(4);  
print(emp_1.salary_up);

emp_3 = Employee.create_employee('Nguyen', 'B', 70000, 28)
print(emp_3.salary) # Output: 70000
còn có thể thông qua phương thức bất kì để tạo ra đối tượng (cách này ít được dùng)

# Static Method:

- không nhận tham số đặc biệt nào (không phải self hay cls)
- là 1 phương thức bình thường, gọi qua class nhưng k cần tạo instance. Static method k thuộc vào dữ liệu của class hoặc instance
- thường sài khi phương thức k cần truy cập vào bất kỳ thông tin nào của class hoặc instance
- thường dc khai báo với decorator là: @staticmethod

ví dụ:
class Number:
def **init**(self, a,b):
self.a = a
self.b = b

    @staticmethod
    def sum():
        print (1 + 2)

Number.sum()

vẫn có thể truyền tham số vào sum: ví dụ:
class Number:
def **init**(self, a,b):
self.a = a
self.b = b

    @staticmethod
    def sum(a,b):
        return a+b

print(Number.sum(3,7))

Ngoài ra còn có 1 số method đặc biệt trong class (special methods)

# **repr**: nó sẽ trả về 1 string

class Employee:
salary_up = 2;
nums_of_oject = 0;
def **init**(self, fname,lname, salary,age):
self.fname = fname
self.lname = lname
self.salary = salary
self.age = age
Employee.nums_of_oject += 1

    def get_fullname(self):
        return self.fname + ' ' + self.lname
    def incre_salary(self):
        self.salary = self.salary * self.salary_up

    def __repr__(self):
        return "employee"

emp_1 = Employee('Anh', 'Huy', 50000, 30)
print(emp_1)  
==> trước khi có **repr** thì print(emp_1) in ra <**main**.Employee object at 0x0000018B49046CF0> mà k có thông tin gì cả
còn sau khi có **repr** thì sẽ in ra dc Employee(Anh, Huy, 50000, 30)

class Employee:
salary_up = 2;
nums_of_oject = 0;
def **init**(self, fname,lname, salary,age):
self.fname = fname
self.lname = lname
self.salary = salary
self.age = age
Employee.nums_of_oject += 1

    def get_fullname(self):
        return self.fname + ' ' + self.lname
    def incre_salary(self):
        self.salary = self.salary * self.salary_up

    def __repr__(self):
        return f"Employee({self.fname}, {self.lname}, {self.salary}, {self.age})"

    def __str__(self):
        return f"{self.get_fullname()}, Age: {self.age}"

emp_1 = Employee('Anh', 'Huy', 50000, 30)

print(emp_1)

# sau khi có thêm phương thức **str** thì sẽ in ra kết quả là Anh Huy, Age: 30 vì print llúc này đang nhận mặc định là phương thức **str**

nếu muốn in 2 giá trị ra thì
print(str(emp_1))
print(repr(emp_1))

# **repr** là để cho dev kiểm tra xem có trả về đúng thuộc tính hay không còn hàm **str** dùng để in ra cho người dùng xem

# phương thức add và len

ví dụ:
class Employee:
salary_up = 2;
nums_of_oject = 0;
def **init**(self, fname,lname, salary,age):
self.fname = fname
self.lname = lname
self.salary = salary
self.age = age
Employee.nums_of_oject += 1

    def __add__(self, other):
        return self.salary + other.salary
    def __len__(self):
        return len(self.get_fullname())

emp_1 = Employee('Anh', 'Huy', 50000, 30)
emp_2 = Employee('Nguyen', 'A', 60000, 25)
print(emp_1 + emp_2) # Output: 110000 (50000 + 60000)
print(len(emp_1)) # Output: 8 (length of 'Anh Huy')

# string method

# List Methods

    mylist = ['apple', 'banana', 'cherry']

print(mylist[1]) # Output: banana

mylist.append('orange') # thêm phần tử vào cuối danh sách
print(mylist) # Output: ['apple', 'banana', 'cherry', 'orange']

mylist2 = mylist.copy() # sao chép danh sách
print(mylist2) # Output: ['apple', 'banana', 'cherry', 'orange']

# Đếm số lần xuất hiện của 1 phần tử trong danh sách

print(mylist2.count('banana')) # Output: 1

# Thêm nhiều phần tử vào cuối danh sách

mylist2.extend(['kiwi', 'mango'])
print(mylist2) # Output: ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango']

# Thêm phần tử vào vị trí cụ thể trong danh sách

mylist2.insert(2, 'grape')
print(mylist2) # Output: ['apple', 'banana', 'grape', 'cherry', 'orange', 'kiwi', 'mango']

# Tim vị trí của phần tử trong danh sách

print(mylist2.index('kiwi')) # Output: 5

# Xóa phần từ theo vị trí

mylist2.pop(3) # Removes 'cherry'
print(mylist2) # Output: ['apple', 'banana', 'grape', 'orange', 'kiwi', 'mango']

# Xóa phần tử theo giá trị

mylist2.remove('banana') # Removes 'banana'
print(mylist2) # Output: ['apple', 'grape', 'orange', 'kiwi', 'mango']

# đảo ngược thứ tự của danh sách

mylist2.reverse()
print(mylist2) # Output: ['mango', 'kiwi', 'orange', 'grape', 'apple']

# Sắp xếp danh sách

mylist2.sort()
print(mylist2) # Output: ['apple', 'grape', 'kiwi', 'mango', 'orange']

# Xóa tất cả phần tử trong danh sách

mylist2.clear()
print(mylist2) # Output: []
print(mylist)

# Tuple Methods

# Set Methods

# Dictionary Methods

# Dunder Methods

# Abstract Method (@abstractmethod)

instance: Tương tác với dữ liệu của instance
class: Khi muốn tạo object theo cách riêng (factory method). Hoặc làm gì đó ảnh hưởng đến toàn bộ class.
static: Khi viết hàm nhưng muốn để nằm tập trung trong class cho gọn, mà không đụng đến dữ liệu của class hay object.

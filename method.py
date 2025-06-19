mylist = ['apple', 'banana', 'cherry']
print(mylist[1])    # Output: banana

mylist.append('orange') # thêm phần tử vào cuối danh sách
print(mylist)       # Output: ['apple', 'banana', 'cherry', 'orange']

mylist2 = mylist.copy() # sao chép danh sách
print(mylist2)      # Output: ['apple', 'banana', 'cherry', 'orange']

# Đếm số lần xuất hiện của 1 phần tử trong danh sách
print(mylist2.count('banana'))  # Output: 1

# Thêm nhiều phần tử vào cuối danh sách
mylist2.extend(['kiwi', 'mango'])
print(mylist2)      # Output: ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango']

# Thêm phần tử vào vị trí cụ thể trong danh sách
mylist2.insert(2, 'grape')
print(mylist2)      # Output: ['apple', 'banana', 'grape', 'cherry', 'orange', 'kiwi', 'mango']

# Tim vị trí của phần tử trong danh sách
print(mylist2.index('kiwi'))  # Output: 5

# Xóa phần từ theo vị trí
mylist2.pop(3)      # Removes 'cherry'
print(mylist2)      # Output: ['apple', 'banana', 'grape', 'orange', 'kiwi', 'mango']
# Xóa phần tử theo giá trị
mylist2.remove('banana')  # Removes 'banana'
print(mylist2)      # Output: ['apple', 'grape', 'orange', 'kiwi', 'mango']

# đảo ngược thứ tự của danh sách
mylist2.reverse()
print(mylist2)      # Output: ['mango', 'kiwi', 'orange', 'grape', 'apple']
# Sắp xếp danh sách
mylist2.sort()
print(mylist2)      # Output: ['apple', 'grape', 'kiwi', 'mango', 'orange']

# Xóa tất cả phần tử trong danh sách    
mylist2.clear()
print(mylist2)       # Output: []
print(mylist)



# set và get
class Person:
    name = 'No name'
    def setName(self,new_name):
        self.name = new_name;
    def getName(self):
        return self.name
a=Person();
a.setName('Anh Huy')
print(a.getName())

class Employee:
    salary_up = 2;
    nums_of_oject = 0;
    def __init__(self, fname,lname, salary,age):
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
    def change_salary_up(cls, new_salary_up):
        cls.salary_up = new_salary_up

    @classmethod
    def create_employee(cls, fname, lname, salary, age):
        return cls(fname, lname, salary, age)
    @staticmethod
    def sum():
        print (5 + 10)

emp_1 = Employee('Anh', 'Huy', 50000, 30)
emp_2 = Employee('Nguyen', 'A', 60000, 25)

print(emp_1.salary_up);
print(emp_2.salary_up);

Employee.change_salary_up(3)
print(emp_1.salary_up);
print(emp_2.salary_up);

emp_1.change_salary_up(4);  
print(emp_1.salary_up);

emp_3 = Employee.create_employee('Nguyen', 'B', 70000, 28)
print(emp_3.salary)  # Output: 70000






class Number:
    def __init__(self, a,b):
        self.a = a
        self.b = b
    
    @staticmethod
    def sum():
        print (1 + 2)
    
Number.sum()
emp_1.sum()

class Number:
    def __init__(self, a,b):
        self.a = a
        self.b = b
    
    @staticmethod
    def sum(a,b):
        return a+b
    
print(Number.sum(3,7))

class Employee:
    salary_up = 2;
    nums_of_oject = 0;
    def __init__(self, fname,lname, salary,age):
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
    
    def __add__(self, other):
        return self.salary + other.salary

emp_1 = Employee('Anh', 'Huy', 50000, 30)
emp_2 = Employee('Nguyen', 'A', 60000, 25)
print(emp_1 + emp_2)  # Output: 110000 (50000 + 60000)

print(emp_1)  
print(str(emp_1))
print(repr(emp_1))


import datetime
today = datetime.datetime.now()
print(str(today))  # Output: '2023-10-01 12:34:56.789012'
print(repr(today))  # Output: 'datetime.datetime(2023, 10, 1, 12, 34, 56, 789012)'


class Employee:
    salary_up = 2;
    nums_of_oject = 0;
    def __init__(self, fname,lname, salary,age):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.age = age
        Employee.nums_of_oject += 1
    def get_fullname(self):
        return self.fname + ' ' + self.lname
    def __add__(self, other):
        return self.salary + other.salary
    def __len__(self):
        return len(self.get_fullname())

emp_1 = Employee('Anh', 'Huy', 50000, 30)
emp_2 = Employee('Nguyen', 'A', 60000, 25)
print(emp_1 + emp_2)  # Output: 110000 (50000 + 60000)
print(len(emp_1))  # Output: 8 (length of 'Anh Huy')


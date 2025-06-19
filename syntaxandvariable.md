> > > print("Hello, World!")
> > > Kết quả in ra: Hello, World!

tạo 1 tệp python: python myfile.py

cấu trúc python: thụt lề
Ví dụ:
if 5 > 2:
print("Five is greater than two!")
==> cú pháp đúng in ra kq: Five is greater than two!
if 5 > 2:
print("Five is greater than two!")
==> sai syntax

Variables in Python:
x=5 : int
y=5.5 : float
z="John" : string
X="HuyANH" : Tên biến phân biệt chữ hoa chữ thường. => KQ:HuyAnh
#Tên biến: variables name:
Tên biến phải bắt đầu bằng một chữ cái hoặc ký tự gạch dưới
Tên biến không thể bắt đầu bằng số
Tên biến chỉ có thể chứa các ký tự chữ và số và dấu gạch dưới (Az, 0-9 và \_)
Tên biến phân biệt chữ hoa chữ thường (age, Age và AGE là ba biến khác nhau)
Tên biến không thể là bất kỳ từ khóa Python nào .

# Hợp lệ:

myvar = "John"
my_var = "John"
my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Không hợp lệ:

2myvar = "John"
my-var = "John"
my var = "John"
Camel Case: myVariableName = "John"
Pascal Case: MyVariableName = "John"
Snake Case: my_variable_name = "John"

# Multiple Variables: gán giá trị cho nhiều biến trên một dòng

Example
x, y, z = "Orange", "Banana", "Cherry"
print(x): Orange
print(y): Banana
print(z): Cherry
Có thể gán 1 giá trị cho nhiều biến: x=y=z="Orange"

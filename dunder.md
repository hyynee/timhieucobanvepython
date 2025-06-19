dunder là cái dấu '__' dùng để bắt đầu và kết thúc phương thức, và thường dc sử dụng để nạp chồng.
Ví dụ nnhư:
__new__
__init__
__del__
__str__(seft)
và nhiều cái khác như:
# Numeric magic methods
__trunc__(self): Triển khai hành vi cho math.trunc()
__ceil__(self): Triển khai hành vi cho math.ceil()
__floor__(self): Triển khai hành vi cho math.floor()
__round__(self,n): Triển khai hành vi cho round() tích hợp sẵn
__invert__(self): Triển khai hành vi cho phép đảo ngược bằng toán tử ~.
__abs__(self): Triển khai hành vi cho abs() tích hợp sẵn
__neg__(self): Triển khai hành vi cho phép phủ định
__pos__(self): Triển khai hành vi cho phép toán số học dương đơn phân

# Arithmetic operators
__add__(self, other): Triển khai hành vi cho toán tử + (cộng).
__sub__(self, other): Triển khai hành vi cho toán tử - (trừ).
__mul__(self, other): Triển khai hành vi cho toán tử * (nhân).
__floordiv__(self, other): Triển khai hành vi cho toán tử // (chia phần nguyên).
__truediv__(self, other): Triển khai hành vi cho toán tử / (phép chia thực).
__mod__(self, other): Triển khai hành vi cho toán tử % (modulus).
__divmod__(self, other): Triển khai hành vi cho hàm divmod().
__pow__(self, other): Triển khai hành vi cho toán tử ** (lũy thừa).
__lshift__(self, other): Triển khai hành vi cho toán tử << (chuyển bit trái).
__rshift__(self, other): Triển khai hành vi cho toán tử >> (chuyển bit phải).
__and__(self, other): Triển khai hành vi cho toán tử & (bitwise and).
__or__(self, other): Triển khai hành vi cho toán tử | (bitwise or).
__xor__(self, other): Triển khai hành vi cho toán tử ^ (bitwise xor).
__invert__(self): Triển khai hành vi cho bitwise KHÔNG sử dụng toán tử ~.
__neg__(self): Triển khai hành vi cho phép phủ định bằng toán tử -.
__pos__(self): Triển khai hành vi cho phép phủ định đơn phân bằng toán tử +.


# String Magic Methods
__str__(self): Xác định hành vi khi str() được gọi trên một thể hiện của lớp của bạn.
__repr__(self): Được gọi bằng phương thức repr() tích hợp để trả về biểu diễn có thể đọc được bằng máy của một kiểu.
__unicode__(self): Phương thức này trả về một chuỗi unicode của một kiểu.
__format__(self, formatstr): trả về một kiểu chuỗi mới.
__hash__(self): Phương thức này phải trả về một số nguyên và kết quả của nó được sử dụng để so sánh khóa nhanh trong từ điển.
__nonzero__(self): Xác định hành vi khi bool() được gọi trên một thể hiện của lớp của bạn.
__dir__(self): Phương thức này trả về danh sách các thuộc tính của một lớp.
__sizeof__(self): Phương thức này trả về kích thước của đối tượng.


# Comparison magic methods:
__eq__(self, other): Xác định hành vi cho toán tử bằng, ==.
__ne__(self, other): Xác định hành vi cho toán tử bất đẳng thức, !=.
__lt__(self, other): Xác định hành vi cho toán tử nhỏ hơn, <.
__gt__(self, other): Xác định hành vi cho toán tử lớn hơn, >.
__le__(self, other): Xác định hành vi cho toán tử nhỏ hơn hoặc bằng, <=.
__ge__(self, other): Xác định hành vi cho toán tử lớn hơn hoặc bằng, >=.
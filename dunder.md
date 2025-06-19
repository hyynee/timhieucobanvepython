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
__format__(self, formatstr): trả về một kiểu chuỗi mới.
__hash__(self): Phương thức này phải trả về một số nguyên và kết quả của nó được sử dụng để so sánh khóa nhanh trong từ điển.
__nonzero__(self): Xác định hành vi khi bool() được gọi trên một thể hiện của lớp của bạn.
__dir__(self): Phương thức này trả về danh sách các thuộc tính của một lớp.
__sizeof__(self): Phương thức này trả về kích thước của đối tượng.
    Container methods: __len__, __getitem__, __setitem__, __contains__
    (len: trả về dộ dài: ví dụ như anhhuy thì dộ dài là 6)
    (getiem: lấy phần tử tại vị trí hoặc key ví dụ: obj[1],obj['key'])
    (setitem: gán giá trị cho phần tử tại vị trí đó hoặc key)
    (contains: check xem phẩn tử đó có trong object không)
    Callable objects: __call__: cho object được gọi như một hàm : obj()


    Context managers: __enter__, __exit__

    Attribute access: __getattr__, __setattr__, __delattr__ : get: truy cập thuộc tính , set : gán giá trị cho thuộc tính , del: xóa thuộc tính đó.


# Comparison magic methods:
__eq__(self, other): Xác định hành vi cho toán tử bằng, ==.
__ne__(self, other): Xác định hành vi cho toán tử bất đẳng thức, !=.
__lt__(self, other): Xác định hành vi cho toán tử nhỏ hơn, <.
__gt__(self, other): Xác định hành vi cho toán tử lớn hơn, >.
__le__(self, other): Xác định hành vi cho toán tử nhỏ hơn hoặc bằng, <=.
__ge__(self, other): Xác định hành vi cho toán tử lớn hơn hoặc bằng, >=.


Ví dụ:
class Vidu:
    # Initialization
    def __init__(self, value):
        self.value = value
    # String representation
    def __str__(self):
        return f"Vidu với giá trị: {self.value}"
    def __repr__(self):
        return f"Vidu({self.value!r})"
    # Comparison
    def __eq__(self, other):
        if isinstance(other, Vidu):
            return self.value == other.value
        return False
    # Arithmetic operations
    def __add__(self, other):
        if isinstance(other, Vidu):
            return Vidu(self.value + other.value)
        return Vidu(self.value + other)
    # Container protocol
    def __len__(self):
        return len(str(self.value))
    # Callable object
    def __call__(self, multiplier):
        return self.value * multiplier
    # Context manager
    def __enter__(self):
        print("Bắt đầu context")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Kết thúc context")
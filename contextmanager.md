contextmanager: dùng để quản lý tài nguyên 1 cách hiệu quả như ghi file , mở file, đóng file thông qua câu lệnh with

# mở file
with open('foo', 'w') as f:
    f.write('Hora! We opened this file')

# mở va đóng file
f = open('foo', 'w')
try:
    f.write('Hora! We opened this file')
finally:
    f.close()

files = []
for _ in range(10000):
    f = open('foo', 'w')
    f.close()  # Đóng file ngay sau khi mở 
    files.append(f)

with something_that_returns_a_context_manager() as my_resource:
    do_something(my_resource)
    ...
    print('done using my_resource')

with something_that_returns_a_context_manager(): trả về 1 đối tượng contextmanager (ví dụ như open() ==> open('file.txt','r)) 
rồi gán đối tượng cho my_resource để saif trong with
thực hiện các thao tác vs my_resource đọc ghi file, truy vấn db,...
==> python tự gọi phương thức __exit__ của context manager để giải phóng tài nguyên (code kết thúc hoăcj bị lỗi)
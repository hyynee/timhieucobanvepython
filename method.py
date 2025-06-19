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
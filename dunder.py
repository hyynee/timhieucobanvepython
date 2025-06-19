class String:
    
    # khởi tạo
    def __init__(self, string):
        self.string = string
        
# name: biến dc  tự động gán trong python
# main: giá trị mặc định gán cho name trong python
if __name__ == '__main__':
    
    string1 = String('Hello')

    print(string1)

# declare our own string class
class String:
    def __init__(self, string):
        self.string = string 
    def __repr__(self):
        return 'Object: {}'.format(self.string)
    def __add__(self, other):
        return self.string + other
# Driver Code
if __name__ == '__main__':
    string1 = String('Hello')
    print(string1 +' Khầy')
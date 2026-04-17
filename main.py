# CLEAR
class MySet:
    def __init__(self):
        self.data = []

    def clear(self):
        self.data = []

    def show(self):
        print(self.data)

s = MySet()
s.data = [1, 2, 3, 4]

s.show()   

s.clear()
s.show()   

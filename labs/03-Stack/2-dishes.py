class Stack():
    def __init__(self, items = None):
        if items == None:
            self.items = []
        else:
            self.items = items
    def push(self, item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return self.items == []
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
    
inp = input('Enter Input : ').split(',')
w_list = Stack()
f_list = Stack() 

for i in inp:
    temp = i.split(' ')
    while not w_list.isEmpty():
        if w_list.peek() >= int(temp[0]):
            w_list.push(int(temp[0]))
            f_list.push(int(temp[1]))
        elif w_list.peek() < int(temp[0]):
            print(f_list.pop())
            w_list.pop()
    if w_list.isEmpty():
        w_list.push(int(temp[0]))
        f_list.push(int(temp[1]))
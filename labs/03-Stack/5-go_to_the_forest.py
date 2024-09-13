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
        return self.items[-1]
    
inp = input('Enter Input : ').split(',')
tree = Stack()
s = Stack()

def check():
    if tree.isEmpty():
        return 0
    else:
        jn=1
        s.push(tree.pop())
        max = s.peek()
        while not tree.isEmpty():
            if tree.peek() > max:
                jn+=1
                
                s.push(tree.pop())
                max = s.peek()
            else:
                s.push(tree.pop())
        while not s.isEmpty():
            tree.push(s.pop())
        return jn

def s_change():
    while not tree.isEmpty():
        if tree.peek() %2 == 0:
            s.push(tree.pop() - 1)
        else:
            s.push(tree.pop() + 2)
    while not s.isEmpty():
        tree.push(s.pop())

for i in inp:
    temp = i.split()
    if temp[0] == 'A':
        tree.push(int(temp[-1]))
    elif temp[0] == 'B':
        print(check())
    else:
        s_change()
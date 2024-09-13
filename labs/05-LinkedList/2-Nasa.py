class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
    def __str__(self):
        return self.value
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.ram = []

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        p = Node(item)
        if self.head == None:
            self.head = p
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = p
        self.tail = p
        self.ram = []

    def size(self):
        num = 0
        current = self.head
        while current != None:
            num += 1
            current = current.next
        return num

    def pop(self, pos = None):
        num = 0
        current = self.head
        while current != None:
            if pos == None:
                self.head = None
                break
            beforee = current
            current = current.next
            num +=1
            if num == pos:
                beforee.next = current.next
            else:
                num += 1
        
    def backward(self):
        current = self.head
        if current.next != None:
            while current.next.next != None:
                current = current.next
            self.ram.insert(0, current.next)
            current.next = None
            self.tail = current
        
    def forward(self):
        current = self.tail
        if self.ram != []:
            current.next = self.ram.pop(0)
            self.tail = current.next
        
list = []   
L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[0] == "E":
        L.append(i[2:])
        list.append(i[2:])
        C = True
    elif i[:] == "B":
        if L.size() >= 2:
            L.backward()
            list.append(L.tail.value)
        else:
            L.pop()
    elif i[:] == "F":
        L.forward()
        if L.tail.value != list[-1]:
            list.append(L.tail.value)

B = []
current = L.head
while current != None:
    B.insert(0, current.value)
    current = current.next

x = ' -> '
print(f'History : {x.join(list)}')
print(f'BackPath : {x.join(B)}')
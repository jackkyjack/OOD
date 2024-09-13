class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
    def __str__(self):
        return self.value
        

class LinkedList:
    def __init__(self):
        self.head = None
        self.Size = 0

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
        self.Size += 1
        
    def addHead(self, item):
        new_head = Node(item)
        new_head.next = self.head
        self.head = new_head
        self.Size += 1

    def search(self, item):
        current = self.head
        while current != None:
            if current.value == item:
                return True
            current = current.next
        return False

    def index(self, item):
        num = 0
        current = self.head
        while current:
            if current.value == item:
                return num
            num += 1
            current = current.next
        return '-1'

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
            beforee = current
            current = current.next
            num +=1
            if num == pos:
                beforee.next = current.next
            else:
                num += 1
        self.Size -= 1
                
    def insert(self, pos, value):
        num = 0
        current = self.head
        while current != None:
            if pos == 0:
                new_node = Node(value)
                new_node.next = current
                self.head = new_node
                break
            if num == pos:
                new_node = Node(value)
                beforee.next = new_node
                new_node.next = current
                break
            else:
                num += 1
            beforee = current
            current = current.next
        self.Size += 1
            
    def shift_Left(self):
        current = self.head
        temp1 = current.next
        while temp1 != None:
            if str(self.head.next) == '|':
                current.next = temp1.next
                self.addHead('|')
                break
            elif str(temp1) == '|':
                temp2.next = temp1
                current.next = temp1.next
                temp1.next = current
                break
            else:
                temp2 = current
                current = current.next
                temp1 = current.next
        
    def shift_Right(self):
        current = self.head
        temp1 = current
        while current.next != None:
            if str(self.head) == '|':
                temp2 = self.head.next.next
                temp3 = self.head.next
                self.head = temp3
                self.head.next = current
                self.head.next.next = temp2
                return True
            elif str(current) == '|':
                if str(current.next) != 'None':
                    temp2 = current.next
                    temp3 = temp2.next
                    temp1.next = temp2
                    temp2.next = current
                    current.next = temp3
                    return True
                else:
                    return True
            else:
                temp1 = current
                current = current.next
        return False
               
    def Backspace(self):
        current = self.head
        temp1 = current
        while current != None:
            if str(current.next) == '|':
                temp1.next = current.next
                
                break
            else:
                temp1 = current
                current = current.next
        
    def Delete(self):
        current = self.head
        while current != None:
            if str(current) == '|':
                if current.next != None:
                    current.next = current.next.next
                    break
                else:
                    break
            else:
                current = current.next
    
L = LinkedList()
L.append('|')
inp = input('Enter Input : ').split(',')
num = 0

for i in inp:
    mode, value = i.split(' ')[0], i.split(' ')[-1]
    if mode == 'I':
        L.insert(num,value)
        num += 1
    elif mode == 'L':
        L.shift_Left()
        if num == 0:
            num = 0
        else:
            num -= 1
    elif mode == 'R':
        if L.shift_Right():
            num += 1
    elif mode == 'B':
        L.Backspace()
        num -= 1
    elif mode == 'D':
        L.Delete()
print(L)
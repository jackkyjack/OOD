class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
    def __str__(self):
        return self.value
        

class LinkedList:
    def __init__(self):
        self.head = None

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

    def addHead(self, item):
        new_head = Node(item)
        new_head.next = self.head
        self.head = new_head

    def search(self, item):
        current = self.head
        while current != None:
            if current.value == item:
                return 'Found'
            current = current.next
        return 'Not Found'

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

    def pop(self, pos):
        num = 0
        current = self.head
        while current != None:
            beforee = current
            current = current.next
            num +=1
            if pos == 0:
                self.head = current
                return 'Success'
            elif num == pos:
                beforee.next = current.next
                return 'Success'
            else:
                num += 1
        return 'Out of Range'
                
            
L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)
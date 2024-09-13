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
        self.tail = None

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
        self.Size += 1
        
    def addHead(self, item):
        new_head = Node(item)
        new_head.next = self.head
        self.head = new_head
        self.Size += 1
        if not new_head.next :
            self.tail = new_head

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
        
def show_train(x):
    if x.isEmpty():
        return "Empty"
    cur, s = x.head, str(x.head.value) + "->"
    while cur.next != None:
        if not cur.next.next:
            s += str(cur.next.value)
            return s
        else:
            s += str(cur.next.value) + "->"
            cur = cur.next
    return s
        
num, inp = input('Enter input: ').split(' ')
first_bogie = True
list, temp = [], []
number = [int(i) for i in range(1,int(num)+1)]
jn = 0
bogie = LinkedList()
temp = sorted([[int(j) for j in i.split('-')] for i in inp.split(',')])
first, second = temp[0][0], temp[0][1]
bogie.append(first)
list_num = [first]

while temp:
    for k in range(len(temp)):
        check = False
        if second in temp[k]:
            second = temp[k][-1]
            bogie.append(second)
            temp.pop(k)
            if second not in list_num :
                list_num.append(second)
            break
        else:
            check = True
            
    if check:
        list.append(bogie)
        bogie = LinkedList()
        bogie.append(temp[0][0])
        list_num.append(temp[0][0])
        second = temp[0][-1]
    elif not temp:
        list.append(bogie)
  

  
for i in range(len(list)):
    cc = False
    for k in range(len(list)):
        if list[i].tail.value == list[k].head.value:
            cur = list[k].head
            while cur.next != None:
                list[i].append(str(cur.next.value))
                cur = cur.next
            list.pop(k)
            cc = True
            break
    if cc:
        break
    
for i in range(len(list)):
    cc = False
    for k in range(len(list)):
        if list[k].tail.value == list[i].head.value:
            cur = list[i].head
            while cur.next != None:
                list[k].append(str(cur.next.value))
                cur = cur.next
            list.pop(i)
            cc = True
            break
    if cc:
        break
    
# for i in range(len(list)):
#     print(list[i])
        
list_num = sorted(list_num)
# print(list[0],list[1]) #result
# print(list_num)
num = int(num)

for i in range(len(number)):
    cc = True
    for j in range(len(list)):
        check_result = False
        if list[j].head.value == number[i]:
            jn += 1
            print(f'{jn}: {show_train(list[j])}')
            list.pop(j)
            cc = False
            break
        else:
            check_result = True
            cc = False
        
    if check_result and number[i] not in list_num:
        jn += 1
        print(f'{jn}: {number[i]}')
        cc = False
        
    if cc and number[i] not in list_num:
        jn += 1
        print(f'{jn}: {number[i]}')
        
            
print(f'Number of train(s): {jn}')
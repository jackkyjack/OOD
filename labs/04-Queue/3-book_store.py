class Queue():
    def __init__(self, list=None):
        if list == None:
            self.items =[]
        else:
            self.items = list
    def enQueue(self,value):
        return self.items.append(value)
    def deQueue(self):
        return self.items.pop(0)
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    
book,edit = input('Enter Input : ').split('/')

Shelter = Queue()

for i in book.split(' '):
    Shelter.enQueue(i)
    
for j in edit.split(','):
    temp1,value =j.split(' ')[0],j.split(' ')[-1]
    
    if temp1 == 'E':
        Shelter.enQueue(value)
    elif temp1 == 'D':
        Shelter.deQueue()
        
count = 0        
max = Shelter.size()

for i in Shelter:
    Shelter.deQueue()
    if i in Shelter:
        print('Duplicate')
        break
    elif i not in Shelter:
        count += 1
        if count == max:
            print('NO Duplicate')
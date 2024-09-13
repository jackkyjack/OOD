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
    def get(self):
        return [str(i) for i in self.items]
    
inp = input('Enter Input : ').split(',')
check = True

Q = Queue()
U = Queue()

for i in inp:
    temp,value = i.split(' ')[0],i.split(' ')[-1]
    if temp == 'EN':
        Q.enQueue(value)
    elif temp == 'ES':
        U.enQueue(value)
    else:
        if Q.isEmpty() and U.isEmpty():
            print('Empty')
        else:
            if not U.isEmpty():  
                print(U.deQueue())
            elif not Q.isEmpty():
                print(Q.deQueue())
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

Q = Queue()

for i in inp:
    temp = i.split(' ')[0]
    num = i.split(' ')[-1]
    if temp == 'D':
        print(-1) if Q.isEmpty() else print(f'Pop {Q.deQueue()} size in queue is {Q.size()}')
    elif temp == 'E':
        print(f'Add {num} index is {Q.size()}')
        Q.enQueue(num)

print('Empty')if Q.isEmpty() else print(f'Number in Queue is :  {Q.get()}')
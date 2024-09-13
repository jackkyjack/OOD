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
        return [int(i) for i in self.items]
    
inp = input(' ***Cafe***\nLog : ').split('/')

entry,coffee = [],[]
time,max = 0,0
barista1 = Queue()
barista2 = Queue()
q1 = Queue()
q2 = Queue()

for i in inp:
    entry.append(int(i.split(',')[0]))
    coffee.append(int(i.split(',')[-1]))
    
for i in range(len(entry)):
    if barista1.isEmpty():
        last1 = int(entry[i])+int(coffee[i])
        barista1.enQueue(last1)
        q1.enQueue(i+1)
    elif barista2.isEmpty():
        last2 = int(entry[i])+int(coffee[i])
        barista2.enQueue(last2)
        q2.enQueue(i+1)
    else: 
        if last1 < last2:
            while last1 < entry[i]:
                last1 += 1
            if max < (last1-entry[i]):
                max = last1-entry[i]
                waiter = i+1
            last1 += coffee[i]
            barista1.enQueue(last1)
            q1.enQueue(i+1)
        elif last1 > last2:
            while last2 < entry[i]:
                last2 += 1
            if max < (last2-entry[i]):
                max = last2-entry[i]
                waiter = i+1
            last2 += coffee[i]
            barista2.enQueue(last2)
            q2.enQueue(i+1)
        else:
            while last1 < entry[i]:
                last1 += 1
            if max < (last1-entry[i]):
                max = last1-entry[i]
                waiter = i+1
            last1 += coffee[i]
            barista1.enQueue(last1)
            q1.enQueue(i+1)
    if i == len(entry)-1:
        if last1 > last2:
            last_time = last1
        else:
            last_time = last2

total = barista1.size()+barista2.size()
for j in range(last_time+1):
    if j in barista1.get() and j in barista2.get():
        temp1 = q1.deQueue()
        temp2 = q2.deQueue()
        if temp1 > temp2:
            print(f'Time {barista2.deQueue()} customer {temp2} get coffee')
            print(f'Time {barista1.deQueue()} customer {temp1} get coffee')
        else:
            print(f'Time {barista1.deQueue()} customer {temp1} get coffee')
            print(f'Time {barista2.deQueue()} customer {temp2} get coffee')
    else:
        if j in barista1.get():
            print(f'Time {barista1.deQueue()} customer {q1.deQueue()} get coffee')
        elif j in barista2.get():
            print(f'Time {barista2.deQueue()} customer {q2.deQueue()} get coffee')   
            
if max == 1:
    print(f'The customer who waited the longest is : {waiter}\nThe customer waited for {max} minute')
elif max > 1:
    print(f'The customer who waited the longest is : {waiter}\nThe customer waited for {max} minutes')
else:
    print('No waiting')
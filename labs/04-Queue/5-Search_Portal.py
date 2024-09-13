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
    
width, height,lst_input = input('Enter width, height, and room: ').split(' ')
x,xxx,y,yyy,boo,check_f = 0,0,0,0,True,0
lst = Queue()
passed = []

if int(height) != len(lst_input.split(',')):
    print('Invalid map input.')
    exit()
for i in lst_input.split(','):
    if int(width) != len(i):
        print('Invalid map input.')
        exit()

map =[]
for e in lst_input.split(','):
  map.append([i for i in e.split()])    
print("\n",*map,sep = "\n")

def ans():
    print('Found the exit portal.')
    exit()

def show():
    temp_lst = []
    while not lst.isEmpty():
        temp_lst.append(lst.deQueue())
        
    for i in temp_lst:
        lst.enQueue(i)    
    if len(temp_lst) != 0:
        print('Queue: [(',end='')
        print('), ('.join(temp_lst),end='')
        print(')]') 
    else:
        print('Cannot reach the exit portal.')

def search(x,y):
    if (y-1) >= 0 and lst_input.split(',')[y-1][x]=='_': #north
        q = f'{x}, {y-1}'
        if q not in passed:
            lst.enQueue(q)
            passed.append(q)
    elif (y-1) >= int(height) and lst_input.split(',')[y-1][x]=='O':
        ans()
        
    if (x+1) <= int(width)-1 and lst_input.split(',')[y][x+1]=='_': #east
        q = f'{x+1}, {y}'
        if q not in passed:
            lst.enQueue(q)
            passed.append(q)
    elif (x+1) <= int(width)-1 and lst_input.split(',')[y][x+1]=='O':
        ans()

    if (y+1) <= int(height)-1 and lst_input.split(',')[y+1][x]=='_': #south
        q = f'{x}, {y+1}'
        if q not in passed:
            lst.enQueue(q)
            passed.append(q)
    elif (y+1) <= int(height)-1 and lst_input.split(',')[y+1][x]=='O':
        ans()
        
    if (x-1) >=0 and lst_input.split(',')[y][x-1]=='_': #west
        q = f'{x-1}, {y}'
        if q not in passed:
            lst.enQueue(q)
            passed.append(q)
    elif (x-1) >= 0 and lst_input.split(',')[y][x-1]=='O':
        ans()
    show()

for i in lst_input.split(','):
        for j in i:
            if j == 'F':
                print(f'Queue: [({x}, {y})]')#first
                check_f += 1
                search(x,y)
            else:
                x += 1
        y += 1
        x = 0
if check_f :      
    while not lst.isEmpty():
        temp = lst.deQueue()
        xx,yy = int(temp.split(',')[0]),int(temp.split(',')[-1][-1])
        search(xx,yy)
else:
    print('Invalid map input.')
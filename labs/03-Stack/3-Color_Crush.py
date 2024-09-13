class Stack:
    def __init__(self):
        self.stack = []
        self.final =[] 
    def push(self, value):
        self.stack.append(value)
    def pop(self,num):
        return self.stack.pop(num)
    def size(self):
        return len(self.stack)
    def isEmpty(self):
        return True if len(self.stack) == 0 else False
    def lst(self,item):
        return self.stack[item]
    def all(self):
        for item in self.stack:
            self.final.insert(0,item)
        return self.final

inp = input('Enter Input : ').split(' ')
S = Stack()
num = 0
check = True
combo = 0
ans = []

for i in inp:
    S.push(i)

while check and S.size() >= 3:
    if S.lst(num) == S.lst(num+1) and S.lst(num) == S.lst(num+2):
        S.pop(num)
        S.pop(num)
        S.pop(num)
        num = 0
        combo += 1
        if S.size() <3:
            check = False
    else:
        if num != S.size()-3:
            num+=1
        else:
            check =False        

if S.isEmpty():
    if combo <=1 :
        print('0\nEmpty')
    else:
        print(f'0\nEmpty\nCombo : {combo} ! ! !')
else:
    if combo <=1 :
        print(f'{S.size()}')
        print(*S.all(),sep='')
    else:
        print(S.size())
        print(*S.all(),sep='')
        print(f'Combo : {combo} ! ! !')
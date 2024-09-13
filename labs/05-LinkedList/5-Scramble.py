class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

def createLL(LL):
    h = [Node(value) for value in LL]
    return h

def printLL(head):
    x = [head[i].value for i in range(len(head))]
    return ' '.join(x)
    
def SIZE(head):
    return len(head)

def scarmble(head, b, r, size):
    bb = int(len(head) * (b/100))
    rr = int(len(head) * (r/100))
    for i in range(bb):
        head.append(head.pop(0))
        
    print(f'BottomUp {b:.3f} % : ',end = '')
    print(printLL(head))
        
    l1 = [head[i] for i in range(rr)]
    l2 = [head[i] for i in range(rr,len(head))]
    head = []
    l3 = l1.copy()
    l4 = l2.copy()
    for i in range(size):
        if l1:
            head.append(l1.pop(0))
        if l2:
            head.append(l2.pop(0))
    print(f'Riffle {r:.3f} % : ', end='')
    print(printLL(head))
    
    head = []
    
    while l3:
        head.append(l3.pop(0))
    while l4:
        head.append(l4.pop(0))
        
    print(f'Deriffle {r:.3f} % : ', end='')
    print(printLL(head))
        
    for i in range(bb):
        head.insert(0,head.pop())
    print(f'Debottomup {b:.3f} % : ', end='')
    print(printLL(head))
    
    
    
inp1, inp2 = input('Enter Input : ').split('/')
print('-' * 50)
h = createLL(inp1.split())
for i in inp2.split('|'):
    print("Start : {0}".format(printLL(h)))
    k = i.split(',')
    if k[0][0] == "B" and k[1][0] == "R":
        scarmble(createLL(inp1.split()), float(k[0][2:]), float(k[1][2:]), SIZE(h))
    elif k[0][0] == "R" and k[1][0] == "B":
        scarmble(createLL(inp1.split()), float(k[1][2:]), float(k[0][2:]), SIZE(h))
    print('-' * 50)
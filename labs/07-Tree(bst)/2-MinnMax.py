class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):  
        self.root = self._insert(self.root, data)
        return self.root
    
    def _insert(self, node, data):
        if node is None:
            return Node(data)
        else:
            if data < node.data:
                node.left = self._insert(node.left, data)
            else:
                node.right = self._insert(node.right, data)
        return node
            
    def findmin(self):
        cur = self.root
        while cur.left is not None:
            cur = cur.left
        return cur
    
    def findmax(self):
        cur = self.root
        while cur.right is not None:
            cur = cur.right
        return cur
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
print('--------------------------------------------------')
print(f'Min : {T.findmin()}\nMax : {T.findmax()}')
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
        
    def insert(self,data):
        self.root = self._insert(self.root,data)
        return self.root

    def _insert(self, data, node=None):  
        if self.root is None:
            self.root = Node(data)
            
        else:
            
            node = self.root if node is None else node
            
            if data < node.data:
                if node.left is None:
                    node.left = Node(data)
                else: return self._insert(data, node.left)
            
            else:
                
                if node.right is None:
                    node.right = Node(data)  
                else: return self._insert(data, node.right)
            
        return self.root
            
            
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

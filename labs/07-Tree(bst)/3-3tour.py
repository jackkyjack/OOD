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
        self.num = None

    def insert(self, data, node=None):  
        if self.root is None:
            self.root = Node(data)
            
        else:
            
            node = self.root if node is None else node
            
            if data < node.data:
                if node.left is None:
                    node.left = Node(data)
                else: return self.insert(data, node.left)
            
            else:
                
                if node.right is None:
                    node.right = Node(data)  
                else: return self.insert(data, node.right)
            
        return self.root
            
            
    def printTree(self, node, num = None, level = 0):
        if node != None :
            self.printTree(node.right, num , level + 1)
            if num is None:
                print('     ' * level, node)
            else:
                print('     ' * level, (int(node.data)*3) if int(node.data) > num else node) 
            self.printTree(node.left,num ,  level + 1)

T = BST()
inp = input('Enter Input : ').split('/')
lst = [int(i) for  i in inp[0].split()]
for i in lst:
    root = T.insert(i)
T.printTree(root)
print('--------------------------------------------------')
T.printTree(root, int(inp[-1]))


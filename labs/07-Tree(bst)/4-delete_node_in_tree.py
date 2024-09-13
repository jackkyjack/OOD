class Node:
    def __init__(self, data=None): 
        self.data = data if data is not None else None
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
    def __init__(self, node=None): 
        self.root = None if node is not None else None

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
        
    def delete(self, node, data):
        if not node:
            print('Error! Not Found DATA')
            return None
        
        if node.data == data:
            if not node.left and not node.right:
                if self.root == node:
                    self.root = None
                return None
            if not node.left and node.right:
                if self.root.data == data:
                    self.root = node.right
                return node.right
            if node.left and not node.right:
                if self.root.data == data:
                    self.root = node.left
                return node.left
            temp = node.right
            while temp.left: temp = temp.left
            node.data = temp.data
            node.right = self.delete(node.right, node.data)
            if self.root.data == data:
                self.root = node.right
            
        elif node.data > data:
            node.left = self.delete(node.left, data)
        else:
            node.right = self.delete(node.right, data)
        
        return node
    
    def findmaxleft(self,val):
        cur = val.left
        while cur.right != None:
            cur = cur.right
        return cur
    
    def findminright(self,val):
        cur = val.right
        while cur.left != None:
            cur = cur.left
        return cur
    
                
def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)


tree = BinarySearchTree()
data = input("Enter Input : ").split(",")
root = None

for i in data:
    if i[0] == 'i':
        print(f'insert {int(i[2:])}')
        root = tree.insert(int(i[2:]))
    elif i[0] == 'd':
        print(f'delete {int(i[2:])}')
        root = tree.delete(root, int(i[2:]))
    printTree90(root)
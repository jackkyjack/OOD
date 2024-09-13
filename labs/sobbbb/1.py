class AVLnode(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        self.height = self.get_height()
    
    def get_height(self, node):
        return -1 if node is None else node.height
    
    def set_height(self):
        left = self.get_height(self.left)
        right = self.get_height(self.right)
        return 1 + max(left, right)
    
    def get_balance(self):
        return self.get_height(self.left) - self.get_height(self.right)
    
class AVLtree(object):
    def __inint__(self):
        self.root = None
        
    def insert(self,data):
        root = self._insert(self.root, data)
        
    def _insert(self,root,data):
        if root is None:
            return AVLnode(data)
        
        if data < root.data:
            root.left = self._insert(root.left, data)
        else:
            root.right = self._insert(root.right, data)
        root = self.rebalance(root)
        return root
    
    def rebalance(self,node):
        if node is None:
            return node
        balance = node.get_balance()
        if balance == -2:
            if node.right.get_balance() == 1:
                node.right = self.rotate_right(node.right)
            node = self.rotate_left(node)
        elif balance == 2 :
            if node.left.get_balance() == 1:
                node.left = self.rotate_left(node.left)
            node = self.rotate_right(node)
        node.set_hight()
        return node
    
    def rotate_right(self,node):
        new_node = node.left
        node.left = new_node.right
        new_node.right = node
        node = new_node
        node.right.set_height()
        node.set_height()
        return node
    
    def rotate_left(self,node):
        new_node = node.right
        node.right = new_node.left
        new_node.left = node
        node = new_node
        node.left.set_height()
        node.set_height()
        return node
    
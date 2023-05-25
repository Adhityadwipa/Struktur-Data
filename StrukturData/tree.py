#Preorder
class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()
    def PreOrderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreOrderTraversal(root.left)
            res = res + self.PreOrderTraversal(root.right)
        return res
        
root = Node(2) #akar
root.left = Node(3) #kiri
root.right = Node(4) #kanan
root.left.left = Node(5) 
root.left.right = Node(6)
root.right.left = Node(7)
root.right.right = Node(8)
#root.PrintTree()
print(root.PreOrderTraversal(root))


#Inorder
class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()
    def InOrderTraversal(self, root):
        res = []
        if root:
            res = res + self.InOrderTraversal(root.left)
            res.append(root.data)
            res = res + self.InOrderTraversal(root.right)
        return res
        
root = Node(2) #akar
root.left = Node(3) #kiri
root.right = Node(4) #kanan
root.left.left = Node(5) 
root.left.right = Node(6)
root.right.left = Node(7)
root.right.right = Node(8)
#root.PrintTree()
print(root.InOrderTraversal(root))


#Postorder
class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()
    def PostOrderTraversal(self, root):
        res = []
        if root:
            res = res + self.PostOrderTraversal(root.left)
            res = res + self.PostOrderTraversal(root.right)
            res.append(root.data)
        return res
        
root = Node(2) #akar
root.left = Node(3) #kiri
root.right = Node(4) #kanan
root.left.left = Node(5) 
root.left.right = Node(6)
root.right.left = Node(7)
root.right.right = Node(8)
root.left.left.left = Node(9)
root.left.right.right = Node(10)
#root.PrintTree()
print(root.PostOrderTraversal(root))
class Node :
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
                
def storeBSTNode(root, nodes):
    if not root :
        return
    storeBSTNode(root.left, nodes)
    nodes.append(root)
    storeBSTNode(root.right, nodes)

def buildTreeUtil(nodes, start, end):
    if start>end:
        return None
    
    mid = (start+end)//2
    node = nodes[mid]
    node.left = buildTreeUtil(nodes, start, mid-1)
    node.right = buildTreeUtil(nodes, mid+1, end)
    return node

def buildTree(root):
    nodes = []
    storeBSTNode(root, nodes)
    n = len(nodes)
    return buildTreeUtil(nodes, 0, n-1)
 
def printTree(root):
    if not root:\
        return
    #print(root.data)
    #printTree(root.left)
    #printTree(root.right)
    print("Akar : "+str(root.data))
    print("Cabang Kiri Akar : "+str(root.left.data))
    print("Cabang Kanan Akar : "+str(root.right.data))
    print("Cabang Kiri Kanan Akar : "+str(root.left.right.data))
    print("Cabang Kanan Kanan Akar : "+str(root.right.right.data))
    print("Cabang Kanan Kiri Akar : "+str(root.right.left.data))
    
    
if __name__ == "__main__":
    root = Node(10)
    root.left = Node(5)
    root.left.left = Node(3)
    root.left.left.left = Node(7)
    root.left.left.left.left = Node(6)
    root.left.left.left.left.left = Node(11)
    root = buildTree(root)
    printTree(root)
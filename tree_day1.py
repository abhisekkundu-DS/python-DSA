class Node:
    def __init__(self,item=None,right=None,left=None):
        self.item=item
        self.left=left
        self.right=right
class BST:
    def __init__(self):
        self.root=None
        self.item=0
    def insert(self,data):
        if not self.root:
            self.root = Node(data)
        else:
            self.root = self.rinsert(self.root, data)

    def rinsert(self,root,data):
        if root is None:
            return Node(data)
        if root.item > self.item:
            root.left = self.rinsert(root.left,data)
        if root.item < self.item:
            root.right = self.rinsert(root.right,data)
        return root

    def inorder(self):
        result = []
        self.rinoder(self.root,result)
        return result
    def rinoder(self,root,result):
        if root:
            self.rinoder(root.left,result)
            result.append(root.item)
            self.rinoder(root.right,result)


first=BST()
first.insert(45)
first.insert(10)
first.insert(5)
first.insert(15)
print(first.inorder())

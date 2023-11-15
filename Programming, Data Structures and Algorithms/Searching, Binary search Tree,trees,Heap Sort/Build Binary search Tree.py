class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
class BST:
    
    def buildBST(self,root,ele):
        if root==None:
            return Node(ele)
        if ele<root.data:
            root.left=self.buildBST(root.left,ele)
        else:
            root.right=self.buildBST(root.right,ele)
            
        return root
    def inorder(self,root):
        if root==None:
            return
        self.inorder(root.left)
        print(root.data)
        self.inorder(root.right)
        
root=None
b=BST()
for ele in [10,5,25,2,7,30]:
    root=b.buildBST(root,ele)
    
b.inorder(root)

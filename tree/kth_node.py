'''
Given a binary search tree, write a function to find the kth smallest element in the tree.

Example :

Input : 
  2
 / \
1   3

and k = 2

Return : 2

As 2 is the second smallest element in the tree.
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def add_left(self,x):
        self.left = TreeNode(x)
    
    def add_right(self,x):
        self.right = TreeNode(x)


def inOrderList(root):
    if root:
        return inOrderList(root.left) + [root.val] + inOrderList(root.right)
    else:
        return []
    
def kthsmallest(root, k):
    return inOrderList(root)[k-1]


if __name__ == "__main__":
    tree = TreeNode(2)
    tree.add_left(1)
    tree.add_right(3)

    print(kthsmallest(tree,2))
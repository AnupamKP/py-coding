class BinaryTree:
    def __init__(self):
        self.root = None

    class Node:
        def __init__(self, data: int):
            self.left = None
            self.right = None
            self.data = data

    def inorder_traversal(self) -> list:
        return self._inorder_traversal(self.root)

    def _inorder_traversal(self, node: Node) -> list:
        if node is not None:
            return self._inorder_traversal(node.left) + [node.data] + self._inorder_traversal(node.right)
        else:
            return []

    def preorder_traversal(self) -> list:
        return self._preorder_traversal(self.root)

    def _preorder_traversal(self, node: Node) -> list:
        if node is not None:
            return [node.data] + self._inorder_traversal(node.left) + self._inorder_traversal(node.right)
        else:
            return []

    def postorder_traversal(self) -> list:
        return self._postorder_traversal(self.root)

    def _postorder_traversal(self, node: Node) -> list:
        if node is not None:
            return self._inorder_traversal(node.left) + self._inorder_traversal(node.right) + [node.data]
        else:
            return []
    
    def levelorder_traversal(self) -> list:
        Q = [self.root]
        result = []

        while Q:
            temp = Q.pop(0)
            result.append(temp.data)
            if temp.left is not None:
                Q.append(temp.left)
            if temp.right is not None:
                Q.append(temp.right)
        
        return result

    def put(self, value: int):
        new_node = self.Node(value)
        if self.root == None:
            self.root = new_node
            return
        Q = [self.root]

        while Q:
            temp = Q.pop(0)

            if temp.left is not None:
                Q.append(temp.left)
            else:
                temp.left = new_node
                break

            if temp.right is not None:
                Q.append(temp.right)
            else:
                temp.right = new_node
                break
    
    def remove(self, value: int):
        if self.root == None:
            return

        if(self.root.data == value):
            self.root = None
            return
        Q = [self.root]

        while Q:
            temp = Q.pop(0)
            if temp.left is not None:
                if temp.left.data == value:
                    temp.left = None
                    break
                else:
                    Q.append(temp.left)
            if temp.right is not None:
                if temp.right.data == value:
                    temp.right = None
                    break
                else:
                    Q.append(temp.right)

if __name__ == "__main__":
    btree = BinaryTree()
    btree.put(4)
    btree.put(5)
    btree.put(7)
    tree_list = btree.inorder_traversal()
    print(tree_list)
    tree_list = btree.preorder_traversal()
    print(tree_list)
    tree_list = btree.postorder_traversal()
    print(tree_list)
    btree.remove(7)
    tree_list = btree.levelorder_traversal()
    print(tree_list)

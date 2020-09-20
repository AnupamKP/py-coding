class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    class Node:
        def __init__(self, data: int, parent):
            self.data = data
            self.parent = parent
            self.left = None
            self.right = None

    def empty(self):
        self.root = None

    def is_empty(self) -> bool:
        return self.root is None

    def put(self, data: int):
        self.root = self._put(self.root, data)

    def _put(self, node: Node, data: int, parent: Node = None) -> Node:
        if node is None:
            node = self.Node(data, parent)
        else:
            if data < node.data:
                node.left = self._put(node.left, data, node)
            elif data > node.data:
                node.right = self._put(node.right, data, node)
            else:
                raise Exception(f"Node with data {data} already exists")

        return node

    def search(self, data: int) -> Node:
        return self._search(self.root, data)

    def _search(self, node: Node, data: int) -> Node:
        if node is None:
            raise Exception(f"Node with data {data} does not exist")
        else:
            if data < node.data:
                node = self._search(node.left, data)
            elif data > node.data:
                node = self._search(node.right, data)

        return node

    def remove(self, data: int):
        node = self.search(data)
        if not node.right and not node.left:
            self._reassign_nodes(node, None)
        elif not node.right and node.left:
            self._reassign_nodes(node, node.left)
        elif node.right and not node.left:
            self._reassign_nodes(node, node.right)
        else:
            lowest_node = self._get_lowest_node(node.right)
            lowest_node.left = node.left
            lowest_node.right = node.right
            node.left.parent = lowest_node
            if node.right:
                node.right.parent = lowest_node
            self._reassign_nodes(node, lowest_node)

    def _reassign_nodes(self, node: Node, new_children: Node):
        if new_children:
            new_children.parent = node.parent

        if node.parent:
            if node.parent.right == node:
                node.parent.right = new_children
            else:
                node.parent.left = new_children
        else:
            self.root = new_children

    def _get_lowest_node(self, node: Node) -> Node:
        if node.left:
            lowest_node = self._get_lowest_node(node.left)
        else:
            lowest_node = node
            self._reassign_nodes(node, node.right)

        return lowest_node

    def exists(self, data: int) -> bool:
        try:
            self.search(data)
            return True
        except Exception:
            return False

    def get_max_data(self) -> int:
        if self.is_empty():
            raise Exception("Binary search tree is empty")

        node = self.root
        while node.right is not None:
            node = node.right

        return node.data

    def get_min_data(self) -> int:
        if self.is_empty():
            raise Exception("Binary search tree is empty")

        node = self.root
        while node.left is not None:
            node = node.left

        return node.data

    def inorder_traversal(self) -> list:
        return self._inorder_traversal(self.root)

    def _inorder_traversal(self, node: Node) -> list:
        if node is not None:
            yield from self._inorder_traversal(node.left)
            yield node
            yield from self._inorder_traversal(node.right)

    def preorder_traversal(self) -> list:
        return self._preorder_traversal(self.root)

    def _preorder_traversal(self, node: Node) -> list:
        if node is not None:
            yield node
            yield from self._preorder_traversal(node.left)
            yield from self._preorder_traversal(node.right)
    
    def postorder_traversal(self) -> list:
        return self._postorder_traversal(self.root)

    def _postorder_traversal(self, node: Node) -> list:
        if node is not None:
            yield from self._postorder_traversal(node.left)
            yield from self._postorder_traversal(node.right)
            yield node

if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.put(4)
    bst.put(5)
    bst.put(7)
    bst.put(8)
    tree_list = [el.data for el in bst.inorder_traversal()]
    print(tree_list)
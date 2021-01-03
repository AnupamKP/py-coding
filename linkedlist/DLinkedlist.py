# Q. Design an Double linkedlist using oop and have basic capabilities of add , delete and get methods

class DLinkedList:
    class Node:
        def __init__(self, val: int):
            """
            Initialize the double link node class , to be used in this main class.
            """
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self):
        """
        Initialize linkled list datastructure.
        """
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index >= self.size or index < 0:
            return -1

        curr = self.head
        for _ in range(index):
            curr = curr.next

        return curr.val

    def __str__(self) -> list:
        """
        Get the value of the all the nodes in the linked list. If the linkedlist is empty, return blank.
        """
        if self.size != 0:
            return "<--->".join([str(self.get(index)) for index in range(self.size)])
        else:
            return ""

    def add_at_head(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        first_node_index = 0
        self.add_at_index(first_node_index, val)

    def add_at_tail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        last_node_index = self.size
        self.add_at_index(last_node_index, val)

    def add_at_index(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index >= self.size and index < 0:
            return

        node = self.Node(val)
        curr = self.head

        if index == 0:
            node.next = curr
            node.prev = None
            self.head = node
        else:
            for _ in range(index - 1):
                curr = curr.next

            node.next = curr.next
            node.prev = curr
            curr.next = node

        self.size += 1

    def delete_at_index(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if self.get(index) == -1:
            return
        curr = self.head

        if index == 0:
            self.head = curr.next
            curr.next = None
            curr.prev = None
        else:
            for _ in range(index - 1):
                curr = curr.next

            del_node = curr.next
            curr.next = del_node.next
            del_node.next = None
            del_node.prev = None

        self.size -= 1

def main():
    linkedlist = DLinkedList()
    linkedlist.add_at_head(5)
    linkedlist.add_at_tail(7)
    linkedlist.add_at_index(2,9)
    linkedlist.add_at_head(3)
    linkedlist.delete_at_index(1)
    linkedlist.add_at_tail(11)
    linkedlist.add_at_index(2,8)
    print(linkedlist)

if __name__ == "__main__":
    main()

# Q. Design an queue using linkedlist and have basic capabilities of add , delete and get methods

class LQueue:
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
        Initialize queue datastructure.
        """
        self.front = None
        self.rear = None
        self.size = 0
    
    def enqueue(self,val: int) -> None:
        """
        add a val in the queue 
        """
        node = self.Node(val)
        if self.size == 0:
            self.front = self.rear = node
        else:
            node.prev = None
            node.next = self.front
            self.front.prev = node
            self.front = node
            
        self.size += 1

    def dequeue(self) -> None:
        """
        delete the first element in the queue, if not empty
        """
        if self.size == 0:
            return
        
        curr = self.rear.prev
        curr.next = None
        self.rear = curr
        self.size -= 1

    def get_top(self) -> int:
        """
        get the val present in the queue at the rear
        """
        curr = self.rear
        if self.size == 0:
            return -1
        
        return curr.val

def main():
    queue = LQueue()
    queue.enqueue(5)
    queue.enqueue(7)
    queue.enqueue(9)
    queue.dequeue()
    print("Queue next val: {}".format(queue.get_top()))

if __name__ == "__main__":
    main()
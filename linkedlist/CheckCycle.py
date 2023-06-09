'''
Q. Given a linkedlist head , find whether the linkedlist has a cycle or not.

Hint: Similiar to finding the middle of the node using 2 nodes
'''

def hasCycle(self, head: ListNode) -> bool:
        slow_node = fast_node = head
        if head == None:
            return False
        else:
            while(fast_node.next != None and fast_node.next.next != None):
                fast_node = fast_node.next.next
                slow_node = slow_node.next
                if fast_node == slow_node:
                    return True
            return False
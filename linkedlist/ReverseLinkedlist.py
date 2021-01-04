'''
Q. Reverse a linklist with single link nodes.

Hint: Use a intermediate stack , since removing top elements of a stack gives a reverse list of the inputs
'''

def reverse_linklist(head: ListNode) -> ListNode :
    current_node = head
    stack = []
    while(current_node.next != None):
        stack.append(current_node)
        current_node = current_node.next
    head = stack.pop(-1)
    current_node = head
    while(len(stack) >= 1):
        top = stack.pop(-1)
        current_node.next = top
        top.next = None
    
    return head


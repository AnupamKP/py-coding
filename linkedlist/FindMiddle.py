'''
Q. Given a linkedlist head , find the middle node of the linkedlist

Logic : Have two pointer as fast_node and slow_node , fast_node moving twice as slow node and when fast node reaches the end of the ll , slow node would be at the middle of the linklist
'''
def find_middle_key(head: ListNode) -> ListNode:
    if head == None:
        return None
    
    fast_node = slow_node = head

    while(fast_node.next != None and fast_node.next.next != None):
        fast_node = fast_node.next.next
        slow_node = slow_node.next
    
    return slow_node
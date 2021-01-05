'''
Q. Given a linkedlist head and kth position , rotate the linkedlist from the kth postition.
'''

def rotate_linklist(head: ListNode, k: int) -> ListNode:
    if head == None:
        return None

    current_node = head
    count = 0
    while(current_node.next != None):
        count += 1
        temp_next = current_node.next
        if count == k:
            current_node.next = None
            current_node = temp_next
        else:
            current_node = current_node.next 
    
    current_node.next = head
    head = current_node

    return head
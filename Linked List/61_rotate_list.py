class ListNode:
    def __init__(self, val=0, next=None):
        self.val  = val
        self.next = next

class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head
        
        len_linked_list = self.lengthLinkedList(head)
        prev_tail, tail = self.findTwoTails(head)

        for _ in range(k % len_linked_list):
            prev_tail.next  = None
            tail.next       = head
            head            = tail
            prev_tail, tail = self.findTwoTails(head)
        
        return head

    def findTwoTails(self, head):
        prev_tail, tail = head, head

        while tail.next:
            prev_tail = tail
            tail      = tail.next
        
        return (prev_tail, tail)
    
    def lengthLinkedList(self, head):
        curr   = head
        length = 0

        while curr:
            length += 1
            curr = curr.next
        
        return length


def create_singly_linked_list(nodes_list):
    if len(nodes_list) == 0:
        return None
    elif len(nodes_list) == 1:
        return ListNode(val=nodes_list[0])
    
    nodes = list()
    for node_val in nodes_list:
        node = ListNode(val=node_val)
        nodes.append(node)
    
    linked_list_head, curr_head = nodes[0], nodes[0]
    for node in nodes[1:]:
        curr_head.next = node
        curr_head      = curr_head.next

    return linked_list_head

def print_linked_list(linked_list):
    if not linked_list:
        print(linked_list)
    else:
        current = linked_list
        while current.next:
            print(current.val, end="->")
            current = current.next
        print(current.val)


nodes_list, k = [0,1,2], 1
linked_list   = create_singly_linked_list(nodes_list)
print_linked_list(linked_list)

sol             = Solution()
new_linked_list = sol.rotateRight(linked_list, k)
print_linked_list(new_linked_list)
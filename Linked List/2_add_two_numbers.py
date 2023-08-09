class ListNode:
    def __init__(self, val=0, next=None):
        self.val  = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        min_len = min(self.lengthLinkedList(l1), self.lengthLinkedList(l2))

        added_llist     = None
        llist_curr_head = None
        carryout        = 0

        for _ in range(min_len):
            curr_sum = (l1.val + l2.val + carryout) % 10
            carryout = (l1.val + l2.val + carryout) // 10

            if added_llist == None:
                added_llist     = ListNode(curr_sum)
                llist_curr_head = added_llist
            else:
                llist_curr_head.next = ListNode(curr_sum)
                llist_curr_head      = llist_curr_head.next

            l1 = l1.next
            l2 = l2.next
        
        none_empty_llist = l1 if l1 != None else l2

        while none_empty_llist != None:
            curr_sum = (none_empty_llist.val + carryout) % 10
            carryout = (none_empty_llist.val + carryout) // 10

            llist_curr_head.next = ListNode(curr_sum)
            llist_curr_head      = llist_curr_head.next
            none_empty_llist     = none_empty_llist.next
        
        if carryout != 0:
            llist_curr_head.next = ListNode(carryout)
        
        return added_llist

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


llist1 = create_singly_linked_list([9,9,9,9,9,9,9])
llist2 = create_singly_linked_list([9,9,9,9])
print_linked_list(llist1)
print_linked_list(llist2)

sol       = Solution()
new_llist = sol.addTwoNumbers(llist1, llist2)
print_linked_list(new_llist)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return head
        
        first, second = head, head.next

        while second:
            if second.val == first.val:
                first.next = second.next
            else:
                first = second
            
            second = second.next
        
        return head
    
    def printLinkedList(self, linked_list):
        current = linked_list
        while current.next:
            print(current.val, end="->")
            current = current.next
        print(current.val)


n1 = ListNode(val=1)
n2 = ListNode(val=1)
n3 = ListNode(val=2)
n4 = ListNode(val=3)
n5 = ListNode(val=3)

linked_list = n1
n1.next     = n2
n2.next     = n3
n3.next     = n4
n4.next     = n5

sol = Solution()
sol.printLinkedList(linked_list)
new_linked_list = sol.deleteDuplicates(linked_list)
sol.printLinkedList(new_linked_list)
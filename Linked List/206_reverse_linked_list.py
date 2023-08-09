class ListNode:
    def __init__(self, val=0, next=None):
        self.val  = val
        self.next = next

class Solution:
    def reverseList(self, head):
        if head is None:
            return head
        
        first  = head
        second = head.next
        while second is not None:
            temp      = second
            second    = second.next
            temp.next = first
            first     = temp
            
            if head.next is not None:
                head.next = None
        
        return first
    
    def printLinkedList(self, linked_list):
        current = linked_list
        while current.next:
            print(current.val, end="->")
            current = current.next
        print(current.val)


l1_n1 = ListNode(val=1)
l1_n2 = ListNode(val=2)
l1_n3 = ListNode(val=3)
l1_n4 = ListNode(val=4)
l1_n5 = ListNode(val=5)

list1      = l1_n1
l1_n1.next = l1_n2
l1_n2.next = l1_n3
l1_n3.next = l1_n4
l1_n4.next = l1_n5

sol = Solution()
sol.printLinkedList(list1)
reverse_list = sol.reverseList(list1)
sol.printLinkedList(reverse_list)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val  = val
        self.next = next

class Solution:
    def middleNode(self, head):
        length = self.lengthLinkedList(head)
        middle_ind = length//2 + 1

        curr_ind = 1
        while curr_ind < middle_ind:
            head     = head.next
            curr_ind = curr_ind + 1
        
        return head
    
    def lengthLinkedList(self, head):
        curr = head
        len  = 0
        while curr:
            len  = len + 1
            curr = curr.next
        
        return len
    
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
l1_n6 = ListNode(val=6)

list1      = l1_n1
l1_n1.next = l1_n2
l1_n2.next = l1_n3
l1_n3.next = l1_n4
l1_n4.next = l1_n5
l1_n5.next = l1_n6

sol = Solution()
sol.printLinkedList(list1)
middle = sol.middleNode(list1)
sol.printLinkedList(middle)
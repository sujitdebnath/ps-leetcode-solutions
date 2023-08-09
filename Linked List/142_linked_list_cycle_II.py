class ListNode:
    def __init__(self, val=0, next=None):
        self.val  = val
        self.next = next

class Solution:
    def detectCycle(self, head):
        node_list = set()

        while head:
            if head in node_list:
                print(head.val)
                return head
            
            node_list.add(head)
            head = head.next
        
        return None


l1_n1 = ListNode(val=3)
l1_n2 = ListNode(val=2)
l1_n3 = ListNode(val=0)
l1_n4 = ListNode(val=-4)

list1      = l1_n1
l1_n1.next = l1_n2
l1_n2.next = l1_n3
l1_n3.next = l1_n4
l1_n4.next = l1_n2

sol = Solution()
print(sol.detectCycle(list1))
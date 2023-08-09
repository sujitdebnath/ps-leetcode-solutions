class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        if list1 is None and list2 is None:
            return None
        elif list1 is not None and list2 is None:
            return list1
        elif list1 is None and list2 is not None:
            return list2

        merge_list = None
        current = None

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                node = ListNode(list1.val)
                list1 = list1.next
            else:
                node = ListNode(list2.val)
                list2 = list2.next
            
            if merge_list is None:
                merge_list = current = node
            else:
                current.next = node
                current = current.next
        
        while list1 is not None:
            node = ListNode(list1.val)
            current.next = node
            current = current.next
            list1 = list1.next
        
        while list2 is not None:
            node = ListNode(list2.val)
            current.next = node
            current = current.next
            list2 = list2.next
        
        return merge_list

    def printLinkedList(self, linked_list):
        current = linked_list
        while current.next:
            print(current.val, end="->")
            current = current.next
        print(current.val)


l1_n1 = ListNode(val=1)
l1_n2 = ListNode(val=2)
l1_n3 = ListNode(val=4)

list1 = l1_n1
l1_n1.next = l1_n2
l1_n2.next = l1_n3

l2_n1 = ListNode(val=0)
l2_n2 = ListNode(val=1)
l2_n3 = ListNode(val=4)
l2_n4 = ListNode(val=6)
l2_n5 = ListNode(val=9)

list2 = l2_n1
l2_n1.next = l2_n2
l2_n2.next = l2_n3
l2_n3.next = l2_n4
l2_n4.next = l2_n5

sol = Solution()
sol.printLinkedList(list1)
sol.printLinkedList(list2)
merge_list = sol.mergeTwoLists(list1, list2)
sol.printLinkedList(merge_list)
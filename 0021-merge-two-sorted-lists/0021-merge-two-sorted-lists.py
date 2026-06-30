# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(-1)
        current = result
        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                new_node = ListNode(list1.val)
                if current == None:
                    current = new_node
                else:
                    current.next = new_node
                    current = current.next
                list1 = list1.next
            elif list2.val < list1.val:
                new_node = ListNode(list2.val)
                if current == None:
                    current = new_node
                else:
                    current.next = new_node
                    current = current.next
                list2 = list2.next
        if list1:
            current.next = list1
        else:
            current.next = list2
        return result.next
                

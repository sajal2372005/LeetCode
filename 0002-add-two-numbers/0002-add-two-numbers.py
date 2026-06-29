# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0
        while list1 or list2 or carry:
            val1 = list1.val if list1 else 0
            val2 = list2.val if list2 else 0
            total = val1+val2+carry
            carry = total//10
            remainder = total%10
            current.next = ListNode(remainder)
            current = current.next
            
            if list1: list1 = list1.next
            if list2: list2 = list2.next
        return dummy.next

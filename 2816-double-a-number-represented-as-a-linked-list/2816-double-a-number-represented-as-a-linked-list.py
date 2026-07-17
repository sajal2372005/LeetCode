# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import sys
sys.set_int_max_str_digits(10000)
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        total = ""
        current = head
        while current:
            total += str(current.val)
            current = current.next
        total = str(int(total)*2)
        Head2 = ListNode()
        current = Head2
        for i in range(len(total)):
            temp = int(total[i])
            current.val = temp
            if i != len(total)-1:
                current.next = ListNode()
            current = current.next
        return Head2

        
        
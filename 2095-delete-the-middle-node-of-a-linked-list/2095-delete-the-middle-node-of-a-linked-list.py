# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # extra = head
        # ans = head
        if head == None or head.next == None:
            return
        # length = 1
        # while(head.next != None):
        #     length +=1
        #     head = head.next
        # length = math.floor(length/2)
        # temp_len = 1
        # while (temp_len < length):
        #     temp_len +=1
        #     extra = extra.next
        # extra.next = extra.next.next
        # return ans

        slow = head
        fast = head.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return head

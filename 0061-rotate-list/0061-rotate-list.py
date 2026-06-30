# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        k = k%(2*10**9 -2)
        for i in range(k):
            if head == None:
                return
            if head.next == None:
                return head
            current = head
            while current.next.next != None:
                current = current.next
            temp = current.next
            current.next = None
            temp.next = head
            head = temp
        return head
        
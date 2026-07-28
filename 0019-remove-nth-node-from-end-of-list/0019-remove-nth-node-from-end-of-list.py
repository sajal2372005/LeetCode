# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        stack = []
        top = -1
        current = dummy
        while current!= None:
            stack.append(current)
            current= current.next
        node_before = stack[len(stack)-n-1]
        node_before.next = node_before.next.next
        return dummy.next
       
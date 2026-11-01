# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        sets = set(nums)
        final = ListNode(-1)
        start = final
        current = head
        while current != None:
            if current.val in sets:
                current = current.next
            else:
                if start == None:
                    start = ListNode(current.val)
                else:
                    start.next = ListNode(current.val)
                    start = start.next
                current = current.next
        return final.next


        
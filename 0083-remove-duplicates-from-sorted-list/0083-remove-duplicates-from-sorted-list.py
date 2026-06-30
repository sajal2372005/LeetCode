# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set()
        if head == None:
            return
        current = head
        nums.add(current.val)
        while current.next != None:
            if current.next.val in nums:
                current.next = current.next.next
            elif current.next.val not in nums:
                nums.add(current.next.val)
                current = current.next
        return head

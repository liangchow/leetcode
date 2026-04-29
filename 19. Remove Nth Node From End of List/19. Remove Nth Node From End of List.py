#
# Problem: 19. Remove Nth Node From End of List
# Difficulty: Medium
# Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/1991384523/
# Language: python3
# Date: 2026-04-29


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next =  head
        left = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next




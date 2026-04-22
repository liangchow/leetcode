#
# Problem: 143. Reorder List
# Difficulty: Medium
# Link: https://leetcode.com/problems/reorder-list/submissions/1984888059/
# Language: python3
# Date: 2026-04-22


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = None
        slow.next = None

        while second:
            nextNode = second.next
            second.next = prev
            prev = second
            second = nextNode

        second = prev
        first = head
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2

        return head
        

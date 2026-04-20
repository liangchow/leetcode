#
# Problem: 206. Reverse Linked List
# Difficulty: Easy
# Link: https://leetcode.com/problems/reverse-linked-list/submissions/1983800868/
# Language: python3
# Date: 2026-04-20


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev

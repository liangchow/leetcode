#
# Problem: 141. Linked List Cycle
# Difficulty: Easy
# Link: https://leetcode.com/problems/linked-list-cycle/submissions/1967179724/
# Language: python3
# Date: 2026-04-02


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = f = head

        while f and f.next:
            s = s.next
            f = f.next.next
            if s == f:
                return True
        
        return False

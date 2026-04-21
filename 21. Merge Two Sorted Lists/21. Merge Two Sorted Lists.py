#
# Problem: 21. Merge Two Sorted Lists
# Difficulty: Easy
# Link: https://leetcode.com/problems/merge-two-sorted-lists/submissions/1984188819/
# Language: python3
# Date: 2026-04-21


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        tail = res

        while list1 and list2:
            if list1.val >= list2.val:
                tail.next = list2
                list2 = list2.next
            else:
                tail.next = list1
                list1 = list1.next
            tail = tail.next

        if list1:
            tail.next = list1
        else:
            tail.next = list2
        return res.next

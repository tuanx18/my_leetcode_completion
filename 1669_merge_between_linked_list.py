# [MEDIUM] https://leetcode.com/problems/merge-in-between-linked-lists
# Completed 2026/05/02
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        dummy = ListNode(0, list1)
        prev = dummy
        curr = dummy.next
        i = 0
        while curr and curr.next:
            if i == a:
                prevA = prev
            if i == b:
                prevB = curr.next
            prev = curr
            curr = curr.next
            i += 1

        dummy2 = list2
        while dummy2:
            if not dummy2.next:
                dummy2.next = prevB
                break
            dummy2 = dummy2.next
        
        prevA.next = list2
        return list1
        
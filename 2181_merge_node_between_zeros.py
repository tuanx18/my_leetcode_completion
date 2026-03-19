# [MEDIUM] https://leetcode.com/problems/merge-nodes-in-between-zeros/
# Completed 2026/03/13

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        dummy = dummy.next
        ph = ListNode(0)
        ans = ph
        running = 0

        while dummy:
            if dummy.val == 0:
                new = ListNode(running)
                running = 0
                ph.next = new
                ph = ph.next
            else:
                running += dummy.val
            dummy = dummy.next
        return ans.next

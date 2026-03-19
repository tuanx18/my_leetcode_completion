# [MEDIUM] https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points
# Completed 2026/02/22

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        curr = head
        prev = None
        nxt = curr.next
        node_count = 0
        crit = []
        res = [-1, -1]

        while curr:
            if curr.next and prev:
                nxt = curr.next
                if curr.val < prev.val and curr.val < nxt.val:
                    crit.append(node_count)
                if curr.val > prev.val and curr.val > nxt.val:
                    crit.append(node_count)
            prev = curr
            curr = curr.next
            node_count += 1

        if len(crit) == 1:
            return res
        
        final = []
        for n in range(1, len(crit)):
            gap = abs(crit[n] - crit[n-1])
            final.append(gap)
        
        if not final:
            return res
        
        res[0] = min(final)
        res[1] = crit[-1] - crit[0]

        return res
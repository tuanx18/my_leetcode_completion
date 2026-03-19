# https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/
# Completed 2026/02/22
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        dummy = ListNode(0, head)
        curr = dummy.next
        prev = None

        while curr:
            if not prev:
                prev = curr
            else:
                new_val = gcd(prev.val, curr.val)
                node = ListNode(new_val, curr)
                prev.next = node
            prev = curr
            curr = curr.next
        return dummy.next
            
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        values = []
        while head:
            values.append(head.val)
            head = head.next
        values.sort()
        dummy = ListNode(0)
        res = dummy
        for i in values:
            node = ListNode(i)
            dummy.next = node
            dummy = dummy.next
        return res.next
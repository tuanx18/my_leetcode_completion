class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        prev = None
        res = 0
        for ch in s:
            if not prev:
                prev = ord(ch)
            else:
                curr = ord(ch)
                to_add = abs(curr - prev)
                res += to_add
                prev = curr
        return res

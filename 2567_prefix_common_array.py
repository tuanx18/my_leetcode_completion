# [MEDIUM] https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/
# Completed 2026/02/22
class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        seta = set()
        setb = set()
        res = []
        for i in range(len(A)):
            seta.add(A[i])
            setb.add(B[i])
            
            inter = seta & setb
            res.append(len(inter))
        return res
        
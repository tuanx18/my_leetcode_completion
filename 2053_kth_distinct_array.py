# [EASY] https://leetcode.com/problems/kth-distinct-string-in-an-array
# Completed 2026/04/13
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        seen = {}
        for ch in arr:
            seen[ch] = seen.get(ch, 0) + 1
        
        res = ""
        
        for key, val in seen.items():
            if val == 1 and k == 1:
                res = key
                break
            elif val == 1:
                k -= 1
        return res
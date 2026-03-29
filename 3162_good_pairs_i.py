# [EASY] https://leetcode.com/problems/find-the-number-of-good-pairs-i/
# Completed 2026/03/29
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        news = [i * k for i in nums2]
        ans = 0
        for x in nums1:
            for y in news:
                if x % y == 0:
                    ans += 1
        return ans
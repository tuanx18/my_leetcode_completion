# [EASY] https://leetcode.com/problems/sum-of-all-odd-length-subarrays/
# Completed 2026/03/17
class Solution:
    @staticmethod
    def sumOddLengthSubarrays(arr: list[int]) -> int:
        ln = 1
        res = 0
        while ln <= len(arr):
            l = 0
            r = l + ln
            while r <= len(arr):
                print(arr[l:r])
                res += sum(arr[l:r])
                l += 1
                r += 1
            ln += 2
        return res

arr = [1,4,2,5,3]
# Output: 58
sol = Solution.sumOddLengthSubarrays(arr)
print(sol)
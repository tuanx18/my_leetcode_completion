# [EASY] https://leetcode.com/problems/special-array-i
# Completed 2026/04/04
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        is_odd = True if nums[0] % 2 == 1 else False
        for i in nums[1:]:
            if is_odd and i % 2 == 1:
                return False
            elif not is_odd and i % 2 == 0:
                return False
            else:
                if is_odd:
                    is_odd = False
                else:
                    is_odd = True
        return True
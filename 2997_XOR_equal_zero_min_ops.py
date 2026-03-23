# [MEDIUM] https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/
# Completed 2026/03/23
class Solution:
    @staticmethod
    def minOperations(nums: list[int], k: int) -> int:
        # cnt_bit = [0] * (len(bin(max(nums))) - 2)
        # for n in nums:
        #     ci = 0
        #     for i in bin(n)[-1:1:-1]:
        #         if int(i) == cnt_bit[ci]:
        #             cnt_bit[ci] = 0
        #         else:
        #             cnt_bit[ci] = 1
        #         ci += 1
        # print(cnt_bit)

        # kb = format(k, "04b")
        # print(kb)

        res = 0
        
        xor = nums[0]
        for i in nums[1:]:
            xor ^= i

        if xor >= k:
            a = bin(xor)[2:]
            b = format(k, f"0{len(bin(xor)[2:])}b")
        else:
            a = format(xor, f"0{len(bin(k)[2:])}b")
            b = bin(k)[2:]
        
        for bit in range(len(a)):
            if a[bit] != b[bit]:
                res += 1
        
        return res
                

nums = [2,1,3,4]
k = 1
sol = Solution.minOperations(nums, k)
print(sol)
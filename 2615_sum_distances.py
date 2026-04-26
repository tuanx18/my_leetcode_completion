# [MEDIUM] https://leetcode.com/problems/sum-of-distances
# Completed 2026/04/23
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        dist = {}
        for i, v in enumerate(nums):
            if v not in dist:
                dist[v] = [i]
            else:
                dist[v].append(i)
        
        res = [0] * len(nums)

        for k, v in dist.items():
            if len(v) == 1:
                res[v[0]] = 0
                continue
            
            prefix = [0] * len(v)
            prefix[0] = v[0]
            for i in range(1, len(v)):
                prefix[i] = prefix[i-1] + v[i]  

            # REPLACE the nested loops with this single loop ⭐
            for i in range(len(v)):
                curr = v[i]

                left_count = i
                left_sum = prefix[i-1] if i > 0 else 0
                left_dist = curr * left_count - left_sum

                right_count = len(v) - i - 1
                right_sum = prefix[-1] - prefix[i]
                right_dist = right_sum - curr * right_count

                res[curr] = left_dist + right_dist   

        return res
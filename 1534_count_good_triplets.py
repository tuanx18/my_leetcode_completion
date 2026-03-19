# [EASY] https://leetcode.com/problems/count-good-triplets
# Completed 2026/03/17  
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        res = 0
        for i in range(0, len(arr) - 2):
            for j in range(i + 1, len(arr) - 1):
                if abs(arr[i] - arr[j]) > a:
                    continue
                else:
                    for k in range(j + 1, len(arr)):
                        if abs(arr[j] - arr[k]) <= b:
                            if abs(arr[k] - arr[i]) <= c:
                                res += 1
                            else:
                                continue
                        else:
                            continue
        return res
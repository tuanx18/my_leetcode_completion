# [EASY] https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
# Completed 2026/02/22

class Solution(object):
    @staticmethod
    def kidsWithCandies(candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_candy = max(candies)
        res = []
        for c in candies:
            if c + extraCandies >= max_candy:
                res.append(True)
            else:
                res.append(False)
        return res
    
candies = [2,3,5,1,3]
extraCandies = 3
sol = Solution.kidsWithCandies(candies, extraCandies)
print(sol)
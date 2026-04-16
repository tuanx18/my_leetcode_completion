# [EASY] https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array
# Completed 2026/04/15

class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if target not in words:
            return -1

        if words[startIndex] == target:
            return 0

        extended = words[startIndex + 1:] + words + words[:startIndex + 1]
        idx = len(words) - 1
        
        counter = 1
        l = idx - 1
        r = idx + 1

        while l >= 0 or r <= len(extended):
            if l >= 0:
                if extended[l] == target:
                    return counter
            if r < len(extended):
                if extended[r] == target:
                    return counter
            counter += 1
            l -= 1
            r += 1
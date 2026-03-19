# [EASY] https://leetcode.com/problems/check-if-the-sentence-is-pangram/
# Completed 2026/03/18
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        not_seen = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
        for ch in sentence:
            if ch in not_seen:
                not_seen.remove(ch)

            if len(not_seen) == 0:
                return True
        return False
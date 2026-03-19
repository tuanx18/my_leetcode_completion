# [EASY] https://leetcode.com/problems/decode-the-message/
# Completed 2026/03/18
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        mapping = {}
        a = 0
        for ch in key:
            if ch == ' ':
                continue
            else:
                if ch not in mapping.keys():
                    mapping[ch] = alphabet[a]
                    a += 1
        
        ans = ''
        for c in message:
            if c == ' ':
                ans += ' '
            else:
                ans += mapping[c]
        return ans

        
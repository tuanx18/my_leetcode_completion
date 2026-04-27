# [EASY] https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/
# Completed 2026/04/27
class Solution:
    def freqAlphabets(self, s: str) -> str:
        mapping = {}
        for i in range(26):
            ch = chr(ord('a') + i)
            n = str(i + 1)
            if i >= 9:
                n += "#"
            mapping[n] = ch 
        
        res = []
        stack = []
        for i in range(len(s)):
            if s[i] != "#":
                if s[i] == "0":
                    res.append("*")
                else:
                    res.append(mapping[str(s[i])])
                stack.append(str(s[i]))
            else:
                char = stack[-2] + stack[-1] + "#"
                res.pop()
                res.pop()
                res.append(mapping[char])
        return "".join(res)


        

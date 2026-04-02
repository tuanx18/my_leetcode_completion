# [MEDIUM] https://leetcode.com/problems/sort-vowels-in-a-string
# Completed 2026/04/02
class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set(["a", "e", "o", "i", "u"])
        res = []
        cha_map = []
        idx = []
        for i in range(len(s)):
            if s[i].lower() in vowels:
                res.append("_")
                idx.append(i)
                cha_map.append((s[i], ord(s[i])))
            else:
                res.append(s[i])
        cha_map.sort(key=lambda x:x[1])
        # print(cha_map)
        for j in range(len(cha_map)):
            res[idx[j]] = cha_map[j][0]
        return ''.join(res)
# [MEDIUM] https://leetcode.com/problems/lexicographically-smallest-equivalent-string
# Completed 2026/04/27
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        L = len(s1)
        
        grouped = []

        for i in range(L):
            a = s1[i]
            b = s2[i]

            found_groups = []

            for gr in grouped:
                if a in gr or b in gr:
                    found_groups.append(gr)

            if not found_groups:
                grouped.append({a, b})

            else:
                merged = {a, b}

                for gr in found_groups:
                    merged |= gr
                    grouped.remove(gr)

                grouped.append(merged)

        mapping = {}
        for chrs in grouped:
            mn = min(chrs)
            for ch in chrs:
                mapping[ch] = mn
        
        res = ""
        for k in baseStr:
            if k not in mapping:
                res += k
            else:
                res += mapping[k]
        return res

# [MEDIUM] https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/
# Completed 2026/04/16
class Solution:
    def garbageCollection(garbage: list[str], travel: list[int]) -> int:
        pref = [travel[0]]
        curr = travel[0]
        for k in range(1, len(travel)):
            curr += travel[k]
            pref.append(curr)
        cnt = [0] * 3
        
        last_found = [0] * 3
        for i in range(len(garbage)):
            s = [ch for ch in garbage[i]]
            if "M" in s: 
                if i != 0:
                    last_found[0] = pref[i-1]
                else:
                    last_found[0] = 0
                cnt[0] += s.count("M")

            if "P" in s: 
                if i != 0:
                    last_found[1] = pref[i-1]
                else:
                    last_found[1] = 0
                cnt[1] += s.count("P")

            if "G" in s: 
                if i != 0:
                    last_found[2] = pref[i-1]
                else:
                    last_found[2] = 0
                cnt[2] += s.count("G")
        print(last_found, cnt)
        
        return sum(last_found) + sum(cnt)
            

garbage = ["G","M"]
travel = [1]
sol = Solution.garbageCollection(garbage, travel)
print(sol)
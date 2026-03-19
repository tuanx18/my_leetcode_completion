# [HARD] https://leetcode.com/problems/maximum-score-words-formed-by-letters/
# Completed 2026/03/16
class Solution:
    @staticmethod
    def maxScoreWords(words: list[str], letters: list[str], score: list[int]) -> int:
        al = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        score_dct = {}
        for i in range(len(al)):
            score_dct[al[i]] = score[i]

        freq = {}
        for j in letters:
            freq[j] = freq.get(j, 0) + 1

        wscore = {}
        for w in words:
            cur = 0
            for ch in w:
                cur += score_dct[ch]
            wscore[w] = cur 
        
        ans = 0
        def backtrack(y, new_freq: dict, curr_score):
            nonlocal ans
            if y >= len(words):
                ans = max(ans, curr_score)
                return 
            
            need = {}
            for p in words[y]:
                need[p] = need.get(p, 0) + 1

            backtrack(y + 1, new_freq, curr_score)

            # check if there are enough letters
            for ch, va in need.items():
                if freq.get(ch, 0) < va:
                    return
                
            # del letters
            for ch, va in need.items():
                freq[ch] -= va
            
            backtrack(y + 1, new_freq, curr_score + wscore[words[y]])
            
            # backtrack
            for ch, va in need.items():
                freq[ch] += va
            
        backtrack(0, freq, 0)
        return ans         

words = ["dog","cat","dad","good"]
letters = ["a","a","c","d","d","d","g","o","o"]
score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
sol = Solution.maxScoreWords(words, letters, score)
print(sol)
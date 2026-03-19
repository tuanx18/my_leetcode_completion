# [EASY] https://leetcode.com/problems/reverse-vowels-of-a-string
# Completed 2026/02/22

class Solution(object):
    @staticmethod
    def reverseVowels(s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'I', 'E', 'O', 'U'}
        index_list = []

        ss = [_ for _ in s]

        for i in range(len(ss)):
            if s[i] in vowels:
                index_list.append(i)
        
        print(ss, index_list)

        def swap(strx, a, b):
            strx[a], strx[b] = strx[b], strx[a]
        
        left = 0
        right = len(index_list) - 1

        while left <= right:
            swap(ss, index_list[left], index_list[right])
            left += 1
            right -= 1
        
        res = ''.join(ss)
        return res

s = "IceCreAm"
sol = Solution.reverseVowels(s)
print(sol)
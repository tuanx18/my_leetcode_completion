# [EASY] https://leetcode.com/problems/hexadecimal-and-hexatrigesimal-conversion
# Completed 2026/05/02
class Solution:
    def concatHex36(self, n: int) -> str:
        m16 = {}
        m36 = {}

        for i in range(16):
            if i <= 9:
                m16[i] = str(i) 
            else:
                m16[i] = str(chr(ord('A') + i - 10))
        
        for i in range(36):
            if i <= 9:
                m36[i] = str(i) 
            else:
                m36[i] = str(chr(ord('A') + i - 10))
        
        a = n ** 2
        b = n ** 3
        resa = ""
        resb = ""

        while a > 0:
            rem = a % 16
            resa = m16[rem] + resa
            a //= 16
            
        while b > 0:
            rem = b % 36
            resb = m36[rem] + resb
            b //= 36 
        
        return resa + resb
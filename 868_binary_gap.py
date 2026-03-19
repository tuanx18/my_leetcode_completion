# Completed 2026/02/22

class Solution(object):
    @staticmethod
    def binaryGap(n):
        """
        :type n: int
        :rtype: int
        """
        stack = []
        max_path = 0
        
        while n > 0:
            bit = n & 1
            if bit == 1 and not stack:
                stack = [1]
            elif bit == 1 and stack:
                max_path = max(max_path, len(stack))
                stack = [1]
            elif bit == 0:
                if stack:
                    stack.append(0)    
            print(stack)        
            n >>= 1
        return max_path
            

# n = 22 # 1 0 1 1 0
n = 22 # 1 0 1
sol = Solution.binaryGap(n)
print(sol)

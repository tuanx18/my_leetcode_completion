# [MEDIUM] https://leetcode.com/problems/evaluate-reverse-polish-notation
# Completed 2026/03/01
class Solution(object):
    @staticmethod
    def evalRPN(tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        def norm(n):
            # -1.647
            res = ''
            sn = str(n)
            for ch in sn:
                if ch == '.':
                    return int(res)
                else:
                    res += ch
            return int(res)
        
        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in ("+", "-", "*", "/"):
                stack.append(int(tokens[i]))
            else:
                x = stack.pop()
                if tokens[i] == "+":
                    stack[-1] += x
                elif tokens[i] == "-":
                    stack[-1] -= x
                elif tokens[i] == "*":
                    stack[-1] *= x
                elif tokens[i] == "/":
                    print(stack[-1] / x)          
                    stack[-1] = norm(stack[-1] / x)
                    print(stack[-1])
        return stack[0]
    
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
sol = Solution.evalRPN(tokens=tokens)
print(sol)
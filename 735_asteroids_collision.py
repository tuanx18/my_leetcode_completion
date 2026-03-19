# [MEDIUM] https://leetcode.com/problems/asteroid-collision
# Completed 2026/03/02
class Solution:
    @staticmethod
    def asteroidCollision(asteroids: list[int]) -> list[int]:
        stack = []
        for a in asteroids:
            if a > 0:
                stack.append(a)
            elif a < 0:
                if not stack:
                    stack.append(a)
                else:
                    if stack[-1] + a == 0:
                        stack.pop()
                    elif stack[-1] + a < 0:
                        i = len(stack) - 1

                        while i >= 0:
                            if stack[i] + a < 0 and stack[i] * a < 0:
                                stack.pop()
                                i -= 1
                                if i == -1:
                                    stack.append(a)
                            elif stack[i] + a == 0:
                                stack.pop()
                                break
                            elif stack[i] + a > 0 and stack[i] * a < 0:
                                break
                            else:
                                stack.append(a)
                                break
        return stack

asteroids = [3,5,-6,2,-1,4]
sol = Solution.asteroidCollision(asteroids)
print(sol)
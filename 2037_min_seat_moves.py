# [EASY] https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone
# Completed 2026/03/17
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        res = 0
        for i in range(len(seats)):
            res += abs(seats[i] - students[i])
        return res
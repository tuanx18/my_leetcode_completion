class Solution(object):
    @staticmethod
    def minimumAbsDifference(arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        min_dis = 2000000
        res = []
        for i in range(len(arr) - 1):
            pair = [arr[i], arr[i + 1]]
            if pair[1] - pair[0] < min_dis:
                min_dis = pair[1] - pair[0]
                res = []
            if pair[1] - pair[0] > min_dis:
                continue
            res.append(pair)
        return res
    
arr = [4,2,1,3]
sol = Solution.minimumAbsDifference(arr)
print(sol)
class Solution(object):
    @staticmethod
    def maxDistance(arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        max_dis = 0
        min_val = arrays[0][0]
        max_val = arrays[0][-1] 

        for i in range(1, len(arrays)):
            first = arrays[i][0]
            last = arrays[i][-1]

            max_dis = max(max_dis, max_val - first, last - min_val)

            max_val = max(last, max_val)
            min_val = min(first, min_val)
        return max_dis
    
arr = [[1,2,3],[4,5],[1,2,3]]
x = Solution.maxDistance(arr)
print(x)
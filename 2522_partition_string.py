class Solution(object):
    @staticmethod
    def minimumPartition(s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s:
            return -1
        
        res = []
        curr = '0'
        for i in range(len(s)):
            if int(s[i]) > k:
                return -1

            if int((curr + s[i]).lstrip('0')) > k:
                res.append(curr.lstrip('0'))
                curr = '0' + s[i]
            else:
                curr += s[i]
        res.append(curr.lstrip('0'))
        print(res)
        return len(res)
    
s = "127442132"
k = 13
res = Solution.minimumPartition(s, k)
print(res)
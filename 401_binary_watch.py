class Solution(object):
    @staticmethod
    def readBinaryWatch(turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        
        ans = []
        for h in range(12):     # hours: 0..11
            for m in range(60): # minutes: 0..59
                if h.bit_count() + m.bit_count() == turnedOn:
                    ans.append(f"{h}:{m:02d}")   # hour no leading zero, minute two digits
        return ans

turnedOn = 1
["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
output = Solution.readBinaryWatch(turnedOn)
print(output)
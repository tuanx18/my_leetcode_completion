class Solution(object):
    @staticmethod
    def findTheDifference(s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        st = list(t)
        for i in s:
            if i in t:
                ind = st.index(i)
                st.pop(ind)
        if st:
            return st[0]
        else:
            return ''
    
s = 'abcd'
t = 'abcde'
sol = Solution.findTheDifference(s, t)
print(sol)
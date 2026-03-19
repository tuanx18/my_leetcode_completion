class Solution(object):
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        res = 0
        char_list = []
        for i in words:
            char_sublist = []
            for ch in i:
                if ch not in char_sublist:
                    char_sublist.append(ch)
            char_sublist.sort()
            char_list.append(char_sublist)
        # return char_list

        for n in range(len(char_list)):
            for m in range(n + 1, len(char_list)):
                if char_list[m] == char_list[n]:
                    res += 1
        return res
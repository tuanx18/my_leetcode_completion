class Solution(object):
    @staticmethod
    def convertToTitle(columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        alphabet = {
        "A": 1,  "B": 2,  "C": 3,  "D": 4,  "E": 5,  "F": 6,
        "G": 7,  "H": 8,  "I": 9,  "J": 10, "K": 11, "L": 12,
        "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18,
        "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24,
        "Y": 25, "Z": 26
        }
        reverse_alpha = {v: k for k, v in alphabet.items()}
        col = int(columnNumber)
        # print(reverse_alpha[3])
        res = ''
        while col > 0:
            col -= 1
            remain = col % 26
            res = reverse_alpha[remain + 1] + res
            col = col // 26
        return res
    
columnNumber = 12423123
x = Solution.convertToTitle(columnNumber)
print(x)

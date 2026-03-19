class Solution(object):
    @staticmethod
    def intToRoman(num):
        """
        :type num: int
        :rtype: str
        """
        res = ''
        while num > 0:
            if num >= 1000:
                m = num // 1000
                num = num % 1000
                res += m * "M"
            if num >= 900:
                num -= 900
                res += "CM"
            if num >= 500:
                num -= 500
                res += "D"
            if num >= 400:
                num -= 400
                res += "CD"
            if num >= 100:
                c = num // 100
                num = num % 100
                res += c * "C"
            if num >= 90:
                num -= 90
                res += "XC"
            if num >= 50:
                num -= 50
                res += "L"
            if num >= 40:
                num -= 40
                res += "XL"
            if num >= 10:
                x = num // 10
                num = num % 10
                res += x * "X"
            if num >= 9:
                num -= 9
                res += "IX"
            if num >= 5:
                num -= 5
                res += "V"
            if num == 4:
                num = 0
                res += "IV"
            if num > 0:
                i = num
                res += i * "I"
                num = 0
        return res
    
num = 3749 # MMMDCCXLIX
x = Solution.intToRoman(num)
print(x)
        
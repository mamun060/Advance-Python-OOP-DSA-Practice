# sum of Digits of String After Convert
class Solution:
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        s = ''.join(str(ord(char) - 96) for char in s)
        for i in range(k):
            s = str(sum(int(char) for char in s))
        return int(s)

print(Solution.getLucky("iiii", 1))

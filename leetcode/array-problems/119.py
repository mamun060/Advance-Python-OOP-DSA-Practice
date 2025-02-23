#Leetcode: 119. Pascal's Triangle II
class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = []
        for i in range(rowIndex + 1):
            res.append([1])
            for j in range(1, i):
                res[i].append(res[i-1][j-1] + res[i-1][j])
            if i != 0:
                res[i].append(1)
        return res[rowIndex]
    

Solution = Solution()
print(Solution.getRow(3))
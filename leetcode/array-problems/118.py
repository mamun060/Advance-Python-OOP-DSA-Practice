# LeetCode: 118. Pascal's Triangle

def PascalTriangle(numRows):
    if numRows == 0:
        return []
    if numRows == 1:
        return [[1]]
    if numRows == 2:
        return [[1], [1, 1]]
    res = [[1], [1, 1]]
    for i in range(2, numRows):
        res.append([1])
        for j in range(1, i):
            res[i].append(res[i-1][j-1] + res[i-1][j])
        res[i].append(1)
    return res

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        res = [[1], [1, 1]]
        for i in range(2, numRows):
            res.append([1])
            for j in range(1, i):
                res[i].append(res[i-1][j-1] + res[i-1][j])
            res[i].append(1)
        return res
        
Solution = Solution()
print(Solution.generate(5))
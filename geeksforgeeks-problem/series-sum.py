class Solution:
    def seriesSum(self, n:int)-> int:
        summation = 0
        for i in range( 1, n + 1 ):
            summation += i 
        return summation


# another way some sum
class Solution2:
    def seriesSum(self, n: int) -> int:
        return n * (n + 1) // 2
    

sumvalue = int(input())
series = Solution
seriestwo = Solution2
series.seriesSum(sumvalue)
print(seriestwo.seriesSum(5))

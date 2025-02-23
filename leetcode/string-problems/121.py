# Leetcode: 121. Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_price = float('inf')
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit
    

Solution = Solution()
print(Solution.maxProfit([7,6,4,3,1]))
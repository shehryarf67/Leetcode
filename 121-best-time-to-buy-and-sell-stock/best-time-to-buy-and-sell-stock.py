class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minimum = float('inf')
        profit = 0

        for i in range(len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
            if prices[i] != minimum and prices[i] > minimum:
                temp = prices[i] - minimum
                if temp > profit:
                    profit = temp
        
        return profit
        

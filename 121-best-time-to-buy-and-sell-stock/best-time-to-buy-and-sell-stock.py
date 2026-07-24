class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        highest = 0
        lowest = float("inf")

        for price in prices:
            if price < lowest:
                lowest = price
            temp = price - lowest
            if temp > highest:
                highest = temp

        return highest


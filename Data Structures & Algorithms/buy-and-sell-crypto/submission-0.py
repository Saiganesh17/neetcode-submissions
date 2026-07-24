class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit= 0
        min_price= float('inf')
        for current_price in prices:
            max_profit= max(max_profit, current_price- min_price)
            min_price= min(min_price, current_price)
        return max_profit
        #Time and space complexity is O(n ) and O(1 ) respectively
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
         pr=0
         for i in range(1, len(prices)):
            if(prices[i] > prices[i-1]):
                pr =  pr + (prices[i]-prices[i-1])
                continue
         return pr
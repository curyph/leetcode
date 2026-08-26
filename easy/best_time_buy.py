class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left = 0
        right = 1
        maxProfit = 0

        while right < len(prices):
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            else:
                left = right
            right += 1
        return maxProfit
    
    
##### KARDENE'S ALGORITHM

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] - buy > profit:
                profit = prices[i] - buy
        return profit
                
                
a = Solution()
b = a.maxProfit([1,2,4,2,5,7,2,4,9,0,9])
print(b)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0

        def dfs(index,profit,holding):
            
            if index == len(prices):
                return 0
            
            if holding:
                skip = dfs(index + 1, profit, True)
                sell = prices[index] - profit
                
                return max(sell, skip)
            else:
                buy = dfs(index+1, prices[index], True)
                skip = dfs(index + 1, profit, False)
            

            return max(buy,skip)

        return dfs(0,0,False)
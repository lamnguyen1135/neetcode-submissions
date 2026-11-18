class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        cur_min = float("inf")
        ans = 0
        for i in range(n):
            if prices[i] < cur_min:
                cur_min = prices[i]
            else:
                ans = max(ans, prices[i] - cur_min)
        print(cur_min)
        return ans

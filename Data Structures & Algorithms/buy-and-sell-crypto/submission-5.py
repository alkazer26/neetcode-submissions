class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_seen = 0

        l = 0
        r = 1

        while r < len(prices):
            if prices[r] - prices[l] >= 0:
                max_seen = max(max_seen, prices[r] - prices[l])
            else:
                l = r
            r += 1

        return max_seen
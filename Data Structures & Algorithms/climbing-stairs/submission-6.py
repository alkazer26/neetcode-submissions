class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[-1] = 1

        for i in range(n - 1, -1, -1):
            ind = 0 if (i + 2) > n else dp[i + 2]
            dp[i] = dp[i + 1] + ind
        
        return dp[0]
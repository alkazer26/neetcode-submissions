class Solution:
    def numDecodings(self, s: str) -> int:
        # don't count number of groups, count number of ways to group
        dp = [0] * (len(s) + 1)
        dp[-1] = 1
        dp[-2] = int(s[-1] != "0")

        for i in range(len(s) - 2, -1, -1):
            if s[i] != "0":
                dp[i] += dp[i + 1]

            if i + 1 < len(s) and 10 <= int(s[i] + s[i + 1]) <= 26:
                dp[i] += dp[i + 2]

        return dp[0]

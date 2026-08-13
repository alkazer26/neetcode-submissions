class Solution:
    def numDecodings(self, s: str) -> int:
        # don't count number of groups, count number of ways to group
        memo = {}

        def recurse(i):
            if i in memo:
                return memo[i]
                
            if i >= len(s):
                return 1

            total = 0
            if i <= len(s) - 1 and s[i] != "0":
                total += recurse(i + 1)
            if i + 1 < len(s) and 10 <= int(s[i] + s[i + 1]) <= 26:
                total += recurse(i + 2)
            
            memo[i] = total
            return memo[i]

        return recurse(0)

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def recurse(i):
            if i in memo:
                return memo[i]

            if i == n:
                return 1
            if i > n:
                return 0
            
            memo[i] = recurse(i + 1) + recurse(i + 2)
            return memo[i]
            
        return recurse(0)
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 0

        for i in range(n):
            next = a + b   
            b = a
            a = next
        
        return next
 
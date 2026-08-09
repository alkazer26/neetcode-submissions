class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}

        def recurse(i):
            if i in memo:
                return memo[i]

            if i == len(nums) - 1:
                return True
            
            if i >= len(nums) or nums[i] == 0:
                return False

            any_possible = False

            for jump_len in range(1, nums[i] + 1):
                res = recurse(i + jump_len)
                any_possible |= res
            
            memo[i] = any_possible 
            return any_possible
        
        return recurse(0)
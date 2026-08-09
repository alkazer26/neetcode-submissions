class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [-1] * len(nums)
        dp[-1] = True
        for i in range(len(nums) - 2, -1, -1):
            any_possible = False
            for j_length in range(1, nums[i] + 1):
                if i + j_length < len(nums):
                    any_possible |= dp[i + j_length]
            
            dp[i] = any_possible
        
        return dp[0]
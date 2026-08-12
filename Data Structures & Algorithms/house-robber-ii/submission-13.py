class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        dp = [0] * len(nums) 
        # effectively missing last element
        dp[0] = nums[0] 
        dp[1] = max(nums[0], nums[1]) 

        for i in range(2, len(dp) - 1):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

        l_max = dp[len(dp) - 2]

        dp[1] = nums[1]
        dp[2] = max(nums[1], nums[2])

        for i in range(3, len(dp)):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        
        r_max = dp[len(dp) - 1]

        return max(l_max, r_max)

# dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
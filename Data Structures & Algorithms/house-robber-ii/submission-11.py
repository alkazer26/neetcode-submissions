class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        dp = [0] * len(nums) 
        # effectively missing last element
        dp[-2] = nums[-2] 
        dp[-3] = max(nums[-2], nums[-3]) 

        for i in range(len(dp) - 4, -1, -1):
            dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])

        print(dp)
        l_max = dp[0]

        dp[-1] = nums[-1]
        dp[-2] = max(nums[-1], nums[-2]) 

        for i in range(len(dp) - 3, 0, -1):
            dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])
        
        print(dp)
        r_max = dp[1]

        return max(l_max, r_max)
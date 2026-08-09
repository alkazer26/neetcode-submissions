class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp = [0] * len(nums)
        # dp[0] = nums[0]

        # for i in range(1, len(dp)):
        #     dp[i] = max(dp[i - 1] + nums[i], nums[i])
        
        a = nums[0]
        max_sum = a

        for i in range(1, len(nums)):
            b = max(a + nums[i], nums[i])
            max_sum = max(max_sum, b)

            a = b   
    
        return max_sum

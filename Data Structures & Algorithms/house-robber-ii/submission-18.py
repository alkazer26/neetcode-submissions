class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        one, two = nums[0], max(nums[0], nums[1])
        # effectively missing last element

        for i in range(2, len(nums) - 1):
            nxt = max(nums[i] + one, two)
            one = two
            two = nxt

        l_max = two

        one, two = nums[1], max(nums[1], nums[2])

        for i in range(3, len(nums)):
            nxt = max(nums[i] + one, two)
            one = two
            two = nxt
        
        r_max = two

        return max(l_max, r_max)

# dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
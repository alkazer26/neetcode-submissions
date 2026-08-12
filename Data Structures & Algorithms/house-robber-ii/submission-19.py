class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        one, two = 0, 0
        # effectively missing last element

        for i in range(len(nums) - 1):
            nxt = max(nums[i] + one, two)
            one = two
            two = nxt

        l_max = two

        one, two = 0, 0
        # effectively missing first element

        for i in range(1, len(nums)):
            nxt = max(nums[i] + one, two)
            one = two
            two = nxt
        
        r_max = two

        return max(l_max, r_max)

# dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
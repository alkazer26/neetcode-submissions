class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        l = 0
        r = 0

        cur_sum = 0

        while r < len(nums):
            cur_sum += nums[r]
            max_sum = max(max_sum, cur_sum)

            if cur_sum < 0:
                l = r + 1
                r += 1
                cur_sum = 0
            else:
                r += 1

        return max_sum

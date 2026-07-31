class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2
            if nums[l] > nums[r] and nums[m] > nums[l]:
                l = m
            elif nums[l] > nums[r] and nums[m] < nums[l]:
                r = m
            elif nums[l] > nums[r] and nums[m] == nums[l]:
                return nums[r]
            else:
                return nums[l]
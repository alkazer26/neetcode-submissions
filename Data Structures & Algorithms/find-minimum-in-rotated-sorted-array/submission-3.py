class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        if nums[l] < nums[r]:
            return nums[l]
            
        while l <= r:
            m = l + (r - l) // 2
            if nums[l] > nums[r]:
                if nums[m] > nums[l]:
                    l = m
                elif nums[m] < nums[l]:
                    r = m
                else:
                    return nums[r]
            else:
                return nums[l]
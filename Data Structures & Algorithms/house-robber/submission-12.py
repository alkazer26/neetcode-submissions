class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        r = nums[-1]
        l = max(nums[-1], nums[-2])

        for i in range(len(nums) - 3, -1, -1):
            nxt = max(nums[i] + r, l)
            r = l
            l = nxt
        
        return l
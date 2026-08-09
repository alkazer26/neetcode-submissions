class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor_1 = 0

        for n in range(0, len(nums) + 1):
            xor_1 ^= n  
        
        for n in nums:
            xor_1 ^= n
        
        return xor_1
        



            
        
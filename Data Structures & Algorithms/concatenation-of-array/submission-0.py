class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        newArr = [0] * len(nums) * 2
        for i in range(0, len(newArr)):
            newArr[i] = nums[i % len(nums)]
        return newArr
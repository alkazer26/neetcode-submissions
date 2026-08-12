class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        memo = {}

        def recurse(i, arr):
            print(i)
            if i > len(arr) - 1:
                return 0
            if i in memo:
                return memo[i]

            memo[i] = max(arr[i] + recurse(i + 2, arr), recurse(i + 1, arr))

            return memo[i]

        a = recurse(0, nums[:-1])
        memo = {}
        b = recurse(0, nums[1:])

        return max(a, b)

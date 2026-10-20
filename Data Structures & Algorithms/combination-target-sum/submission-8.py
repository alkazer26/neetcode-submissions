class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # stop if running sum equals or exceeds target 
        # at each, iterate through current i --> last index of nums

        res = []
        cur = []

        nums.sort()
        
        def backtrack(i, cur_sum):
            if cur_sum == target:
                res.append(cur.copy())
                return

            for j in range(i, len(nums)):
                if cur_sum + nums[j] > target:
                    return 
                cur.append(nums[j])
                backtrack(j, cur_sum + nums[j])
                cur.pop()
        
        backtrack(0, 0)

        return res
                

      

        

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        out = set()

        # recurse
        # base case > target: return
        # base case == target: sort, make tuple, add to set if not already there

        def recurse(total, comb, i):
            if total > target:
                return
            
            if total == target:
                out.add(tuple(sorted(comb)))
                return
            
            for j in range(i, len(nums)):
                recurse(total + nums[j], [*comb, nums[j]], j)
            
        recurse(0, [], 0)

        return list(map(lambda x : list(x), out))

        

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        out = []
        cur = []
        visited = set()

        def recurse():
            if len(cur) == len(nums):
                out.append(cur.copy())
                return

            
            for j in range(len(nums)):
                if nums[j] not in visited:
                    visited.add(nums[j])
                    cur.append(nums[j])
                    recurse()
                    cur.pop()
                    visited.remove(nums[j])

        recurse()
        return out
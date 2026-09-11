class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # decision tree, left is don't add, right is add element i
        # pop when going up from the right, (last recursive call terminates)
        out = []
        cur = []

        def recurse(i):
            if i == len(nums):
                out.append(cur.copy())
                return

            recurse(i + 1)
            cur.append(nums[i])

            recurse(i + 1)
            cur.pop()

        recurse(0)

        return out

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        l_prefix = [0] * n
        l_prefix[0] = nums[0]

        for i in range(1, n):
            l_prefix[i] = nums[i] * l_prefix[i - 1]
        
        r_prefix = [0] * n
        r_prefix[n-1] = nums[n-1]

        for j in range(n - 2, -1, -1):
            r_prefix[j] = nums[j] * r_prefix[j + 1]
        
        out = [0] * n
        for k in range(n):
            if k == 0:
                out[k] = r_prefix[k + 1]
            elif k == n - 1:
                out[k] = l_prefix[k - 1]
            else:
                out[k] = l_prefix[k - 1] * r_prefix[k + 1]
        
        return out

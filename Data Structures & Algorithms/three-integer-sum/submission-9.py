class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_s = sorted(nums)

        n = len(nums_s)

        triplets = []

        for b in range(0, n - 2):
            if b > 0 and nums_s[b] == nums_s[b - 1]:
                continue

            l = b + 1
            r = n - 1  
            

            while l < r:
                triple = [nums_s[b], nums_s[l], nums_s[r]]
                if sum(triple) == 0:
                    triplets.append(triple)
                    l += 1
                    while l < r and nums_s[l] == nums_s[l - 1]:
                        l += 1
                elif sum(triple) > 0:
                    r -= 1
                    while r > l and nums_s[r + 1] == nums_s[r]:
                        r -= 1
                elif sum(triple) < 0:
                    l += 1
                    while l < r and nums_s[l] == nums_s[l - 1]:
                        l += 1
                
        return triplets
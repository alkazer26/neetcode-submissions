class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        max_seen = 0

        while l < r:
            vol = (r - l) * min(heights[l], heights[r])
            max_seen = max(max_seen, vol)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_seen
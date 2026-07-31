class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ranges = [[0, len(heights) - 1] for _ in heights] # [lbound, rbound] (inclusive)
        
        lstack = [] # [height, index]
        for l in range(len(heights)):
            while lstack and lstack[-1][0] > heights[l]:
                ranges[lstack[-1][1]][1] = l - 1
                lstack.pop()
            
            lstack.append([heights[l], l])

        rstack = []
        for r in range(len(heights) - 1, -1, -1):
            while rstack and rstack[-1][0] > heights[r]:
                ranges[rstack[-1][1]][0] = r + 1
                rstack.pop()
            
            rstack.append([heights[r], r])

        max_rect = 0

        for i, pair in enumerate(ranges):
            area = (pair[1] - pair[0] + 1) * heights[i]
            max_rect = max(max_rect, area)
        
        return max_rect
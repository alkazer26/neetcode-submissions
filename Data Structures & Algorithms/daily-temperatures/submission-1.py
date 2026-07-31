class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0] * len(temperatures)
        stack = [] # (index, temp)

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                # if the new temperature is more than a previous temperature,
                # pop and update output array to reflect number of days between them
                out[stack[-1][0]] = i - stack[-1][0]
                stack.pop()
            
            stack.append([i, temp])
        
        return out
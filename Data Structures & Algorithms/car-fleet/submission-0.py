class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        joined = [[p, s] for p, s in zip(position, speed)]
        joined.sort()

        t_stack = []

        for pair in joined:
            pos, speed = pair
            time = (target - pos) / speed
            
            while t_stack and t_stack[-1] <= time:
                t_stack.pop()

            t_stack.append(time)

        return len(t_stack)
        

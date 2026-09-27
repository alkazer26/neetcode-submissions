class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        s_heap = [-s for s in stones]
        heapq.heapify(s_heap)

        while len(s_heap) >= 2:
            x, y = -heapq.heappop(s_heap), -heapq.heappop(s_heap)

            if x > y:
                heapq.heappush(s_heap, -(x - y))
            elif x < y:
                heapq.heappush(s_heap, -(y - x))
            
        if len(s_heap) == 1:
            return -s_heap[0]
        
        return 0
            



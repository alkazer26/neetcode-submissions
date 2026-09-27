class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for p in points:
            x, y = p
            d = math.sqrt(x**2 + y**2)

            heapq.heappush(heap, (-d, p))

            if len(heap) > k:
                heapq.heappop(heap)
        
        return [pair[1] for pair in heap]


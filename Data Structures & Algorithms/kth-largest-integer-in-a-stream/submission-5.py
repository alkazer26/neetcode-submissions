class KthLargest:
    # use a min-heap, with at most k elements
    # whenever we add an element, if we go over k, pop. At the end, return the head of the list

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = nums 
        self.k = k
        heapq.heapify(self.min_heap)

        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)

        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        return self.min_heap[0]



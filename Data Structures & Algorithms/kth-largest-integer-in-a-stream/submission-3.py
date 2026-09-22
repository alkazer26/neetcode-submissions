class KthLargest:


    # use a min-heap, with at most k elements
    # whenever we add an element, if it is larger than the kth (last) of the largest elemensts, we first heappop, then add it, then return the popped. if element added is smaller than the kth (last) of the largest elements, then do not do anything.



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



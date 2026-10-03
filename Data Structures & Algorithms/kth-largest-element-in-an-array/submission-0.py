class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # keep heap of size k
        # add an element
        # if heap exceeds size k, we pop an element

        # top of heap contains kth largest element
        # case 1: 
            # new element is larger than kth largest element
            # then when we add it, the item popped is the top, which is correct

        # case 2:
            # new element is smaller than or equal to the kth largest element
            # then when we add it, the item is propagated to the top
            # then when we pop, the item popped is the same item we added
        
        heap = []

        for n in nums:
            heapq.heappush(heap, n)

            if len(heap) > k:
                heapq.heappop(heap)
        
        return heap[0]
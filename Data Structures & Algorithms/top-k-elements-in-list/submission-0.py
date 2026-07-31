class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        heap = [(-v, k) for (k, v) in freq.items()]
        heapq.heapify(heap)

        output = []

        for i in range(k):
            val = heapq.heappop(heap)[1]
            output.append(val)
        
        return output


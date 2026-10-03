class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1
        
        heap = [-v for v in freq.values()] # max heap, with largest frequency at the top
                                           # represents tasks that are ready to be used
        heapq.heapify(heap)
        aux = deque([]) # represents tasks that are "cooling down" and are currently off-limits

        t = 1
        n_cycles = 0

        while heap or aux:
            while aux and aux[0][1] <= t: # if we can "use" elements from the deque
                val, time = aux.popleft()
                heapq.heappush(heap, val)

            if heap:
                val = heapq.heappop(heap)

                if val + 1 != 0:
                    aux.append((val + 1, t + n + 1))

            n_cycles += 1
            t += 1
        
        return n_cycles

                
        






        heap = []
        aux = deque([])



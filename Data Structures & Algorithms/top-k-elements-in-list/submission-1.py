class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        freq_array = [[] for _ in range(len(nums) + 1)] 

        for key in freq.keys():
            frequency = freq[key]
            freq_array[frequency].append(key)
        
        out = []

        print(freq)
        print(freq_array)
        for i in range(len(freq_array) - 1, -1, -1):
            for num in freq_array[i]:
                if len(out) < k:
                    out.append(num)
                else:
                    return out
        return out
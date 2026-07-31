class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        for key, freq in count.items():
            if freq > 1:
                return True

        return False
        
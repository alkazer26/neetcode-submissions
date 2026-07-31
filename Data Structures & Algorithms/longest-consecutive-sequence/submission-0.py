class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        nums_set = set(nums)

        longest_seq = 1

        for n in nums:
            cur_len = 1
            for i in range(n, len(nums)):
                if (i + 1) in nums_set:
                    cur_len += 1
                else:
                    break

            if cur_len > longest_seq:
                longest_seq = cur_len
        
        return longest_seq
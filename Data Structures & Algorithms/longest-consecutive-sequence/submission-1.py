class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        longest_seq = 0
        
        for n in nums:
            if n - 1 not in nums_set:
                cur_len = 1
                while (n + 1) in nums_set:
                    cur_len += 1
                    n += 1
                
                if cur_len > longest_seq:
                    longest_seq = cur_len
        
        return longest_seq
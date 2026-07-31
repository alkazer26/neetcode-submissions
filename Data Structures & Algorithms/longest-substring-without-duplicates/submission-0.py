class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        l = 0
        r = 1

        # letter: most recent index
        seen = defaultdict(int)
        seen[s[0]] = 0

        max_len = 1

        while r < len(s):
            if s[r] in seen:
                # everything from index seen[s[r]] to index r is invalid
                # so, shift window by incrementing l to seen[s[r]] + 1
                val = seen[s[r]]
                while l <= val:
                    seen.pop(s[l])
                    l += 1 
            else:
                seen[s[r]] = r
                max_len = max(max_len, r - l + 1)
                r += 1
        
        return max_len



        

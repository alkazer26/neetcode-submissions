class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        max_vals = [0, ""]

        for i in range(len(s)):
            l = i - 1
            r = i + 1

            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break

                l -= 1
                r += 1

            pal_len = r - (l + 1)
            if pal_len > max_vals[0]:
                max_vals = [pal_len, s[l + 1: r]]

            l = i
            r = i + 1

            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break

                l -= 1
                r += 1

            pal_len = r - (l + 1)
            if pal_len > max_vals[0]:
                max_vals = [pal_len, s[l + 1: r]]
                
        return max_vals[1]


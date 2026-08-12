class Solution:
    def longestPalindrome(self, s: str) -> str:
    

        max_vals = [0, ""]

        def expand(l, r):
            nonlocal max_vals

            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break

                l -= 1
                r += 1

            pal_len = r - (l + 1)

            if pal_len > max_vals[0]:
                max_vals = [pal_len, s[l + 1 : r]]

        for i in range(len(s)):
            expand((i - 1), (i + 1))
            expand(i, (i + 1))

        return max_vals[1]


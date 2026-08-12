class Solution:
    def countSubstrings(self, s: str) -> str:
        max_vals = [0, ""]
        n_pal = len(s) # each character is a palindrom itself

        def expand(l, r):
            nonlocal max_vals
            nonlocal n_pal

            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                n_pal += 1
                l -= 1
                r += 1

        for i in range(len(s)):
            expand((i - 1), (i + 1))
            expand(i, (i + 1))

        return n_pal


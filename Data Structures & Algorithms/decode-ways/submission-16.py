class Solution:
    def numDecodings(self, s: str) -> int:
        # don't count number of groups, count number of ways to group

        one, two = int(s[-1] != "0"), 1

        for i in range(len(s) - 2, -1, -1):
            nxt = 0 
            if s[i] != "0":
                nxt += one
            if i + 1 < len(s) and 10 <= int(s[i] + s[i + 1]) <= 26:
                nxt += two

            two = one
            one = nxt

        return one

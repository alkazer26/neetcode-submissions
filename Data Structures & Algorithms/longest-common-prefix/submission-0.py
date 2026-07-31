class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        strs = sorted(strs)

        longest = ""

        for i in range(min(len(strs[0]), len(strs[len(strs) - 1]))):
            if strs[0][i] != strs[len(strs)-1][i]:
                break
            longest+= strs[0][i]
        return longest
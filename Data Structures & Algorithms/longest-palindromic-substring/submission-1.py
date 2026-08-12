class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_vals = [0, ""]

        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.isPalindrome(s[i : j + 1]) and (j - i + 1) > max_vals[0]:
                    max_vals = [(j - i + 1), s[i : j + 1]]
        
        return max_vals[1]
    
    def isPalindrome(self, s):
        return s == s[::-1]
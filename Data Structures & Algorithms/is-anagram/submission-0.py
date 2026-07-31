class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seen_s = {}
        seen_t = {}

        for i in range(len(s)):
            if s[i] not in seen_s:
                seen_s[s[i]] = 0
            else:
                seen_s[s[i]] += 1 

            if t[i] not in seen_t:
                seen_t[t[i]] = 0
            else:
                seen_t[t[i]] += 1 
        print(seen_s, seen_t)
        for char in seen_s:
            if char not in seen_t or seen_s[char] != seen_t[char]:
                return False
        return True

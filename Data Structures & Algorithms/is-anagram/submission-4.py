class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = defaultdict(int)
        hash_t = defaultdict(int)

        for c_s in s:
            hash_s[c_s] += 1
        
        for c_t in t:
            hash_t[c_t] += 1

        return hash_s == hash_t
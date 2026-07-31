class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = defaultdict(int)
        hash_t = defaultdict(int)

        for c_s in s:
            hash_s[c_s] += 1
        
        for c_t in t:
            hash_t[c_t] += 1

        for char_s, freq_s in hash_s.items():
            if freq_s != hash_t[char_s]:
                return False

        for char_t, freq_t in hash_t.items():
            if freq_t != hash_s[char_t]:
                return False

        return True
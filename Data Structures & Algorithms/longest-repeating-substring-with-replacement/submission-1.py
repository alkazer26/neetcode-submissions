class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 1

        # character : frequency in current window from s[l: r + 1]
        freq = defaultdict(int)
        freq[s[l]] = 1

        # character with max frequency
        max_freq = 1

        max_len = 1

        while r < len(s):
            freq[s[r]] += 1
         
            max_freq = max(max_freq, freq[s[r]])

            w_len = r - l + 1

            # if number of replacements is at most k
            if w_len - max_freq <= k:
                max_len = max(max_len, w_len)

            # number of replacements exceeds k
            else:
                freq[s[l]] -= 1
                l += 1

            r += 1

        return max_len

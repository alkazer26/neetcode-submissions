class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            enc_word_len = len(word)
            encoded += f"{enc_word_len}#{word}"

        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        
        l = 0

        while l < len(s):
            dec_word_len = ""
            
            while s[l] != "#":
                dec_word_len += s[l]
                l += 1
            
            l -= 1
            dec_word_len = int(dec_word_len)

            word_decoded = s[l + 2 : l + 2 + dec_word_len]

            decoded.append(word_decoded)
            l += 2 + dec_word_len
        
        return decoded


class Solution:
    def countBits(self, n: int) -> List[int]:
        out = []
        filter = 1

        for i in range(n + 1):
            res = 0
            for b in range(i.bit_length()):
                res += (i >> b) & filter
            
            out.append(res)
        
        return out
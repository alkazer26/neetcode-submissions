class Solution:
    def countBits(self, n: int) -> List[int]:
        out = []

        for i in range(n + 1):
            filter = 1
            res = 0
            for b in range(i.bit_length()):

                res += (i & filter) >> b
                filter = filter << 1
            
            out.append(res)
        
        return out
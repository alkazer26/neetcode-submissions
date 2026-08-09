class Solution:
    def countBits(self, n: int) -> List[int]:
        out = [0]
        bin = 2

        for i in range(1, n + 1):
            if i >= 2 * bin:
                bin *= 2

            out.append(1 + out[i - bin])

        return out



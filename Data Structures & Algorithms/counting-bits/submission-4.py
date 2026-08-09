class Solution:
    def countBits(self, n: int) -> List[int]:
        out = [0]

        for i in range(1, n + 1):
            out.append(1 + out[i - (2 ** math.ceil(math.log(i, 2)))])

        return out



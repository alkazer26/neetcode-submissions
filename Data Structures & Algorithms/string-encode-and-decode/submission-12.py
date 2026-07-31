class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for s in strs:
            length = len(s)
            out += str(length)+"#"+s
        print(out)
        return out

    def decode(self, s: str) -> List[str]:
        s_copy = s
        out = []
        # 4#neet
        # 012345

        while len(s_copy) > 0:
            char_index = 0
            length_string = ""
            print(s_copy)
            while s_copy[char_index] != "#":
                length_string+=s_copy[char_index]
                char_index+=1
            print(length_string)
            length_value = int(length_string)
            print(char_index)
            out.append(s_copy[char_index+1:char_index+1 + length_value])
            s_copy = s_copy[char_index+length_value+1:]

        print(out)
        return out

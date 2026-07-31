class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        map = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for char in s:
            print(char)
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
                print("appeneded")
            elif not stack or stack[-1] != map[char]:
                return False
            else:
                stack.pop()
            

        return len(stack) == 0
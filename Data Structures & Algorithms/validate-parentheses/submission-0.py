class Solution:
    def isValid(self, s: str) -> bool:
        paran = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            if char in paran:
                top = stack.pop() if stack else '#'

                if paran[char] != top:
                    return False

            else:
                stack.append(char)

        return len(stack) == 0

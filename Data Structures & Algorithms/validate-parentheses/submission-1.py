class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        check = {")": "(", "}": "{", "]": "["}
        stack = []
        for c in s:
            if c in {"(", "{", "["}:
                stack.append(c)
            else:
                if not stack or stack[-1] != check[c]:
                    return False
                else:
                    stack.pop()
        return not stack
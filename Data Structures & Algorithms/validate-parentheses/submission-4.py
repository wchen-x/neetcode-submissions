class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ")" : "(", "]" : "[", "}" : "{"
        }

        stack = []

        for i in s:
            if i not in pairs:
                stack.append(i)
            else:
                if not stack:
                    return False
                elif stack.pop() != pairs[i]:
                    return False
        return not stack

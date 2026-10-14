class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {
            '}' : '{',
            ')' : '(',
            ']' : '['
        }

        for c in s:
            if c in match.values():
                stack.append(c)
            else:
                if not stack:
                    return False
                if stack.pop() != match[c]:
                    return False

        return len(stack) == 0
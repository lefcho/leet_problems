class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_close = {
            '(': ')',
            '{': '}',
            '[': ']',
        }

        for bracket in s:
            if bracket in open_close:
                stack.append(bracket)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if open_close[top] != bracket:
                    return False


        if stack:
            return False
        else:
            return True
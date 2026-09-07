class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        for bracket in s:
            if bracket in hashmap:
                # Closing bracket
                if not stack:
                    return False
                top = stack.pop()
                if hashmap[bracket] != top:
                    return False
            else:
                # Opening bracket
                stack.append(bracket)
        if stack:
            return False
        else:
            return True
        
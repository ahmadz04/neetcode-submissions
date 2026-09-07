class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ('+', '-', '*', '/'):
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    # add
                    stack.append(a + b)
                elif token == '-':
                    # subtrack
                    stack.append(a - b)
                elif token == '*':
                    # times
                    stack.append(a * b)
                elif token == '/':
                    stack.append(int(a / b))
            else:
                stack.append(int(token))
        return stack[0]


        
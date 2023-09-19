class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operations = {
            "+": lambda y, x: x + y,
            "-": lambda y, x: x - y,
            "*": lambda y, x: x * y,
            "/": lambda y, x: int(x / y),
        }
        stack = []

        for token in tokens:
            if token in operations:
                token = operations[token](stack.pop(), stack.pop())
            stack.append(int(token))

        return stack.pop()

class Solution:
    def decodeString(self, s: str) -> str:
        stack = deque()

        for c in s:
            if c != "]":
                stack.append(c)
            else:
                word = ""
                times = ""

                while stack and stack[-1] != "[":
                    word = stack.pop() + word
                stack.pop()

                while stack and stack[-1].isdigit():
                    times = stack.pop() + times
                times = int(times)

                stack.append(word * times)

        return "".join(stack)

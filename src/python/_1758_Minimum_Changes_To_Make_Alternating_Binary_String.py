class Solution:
    def minOperations(self, s: str) -> int:
        correct = 0

        flag = True

        for c in s:
            if flag:
                correct += c == "0"
            else:
                correct += c == "1"
            flag = not flag

        return min(correct, len(s) - correct)

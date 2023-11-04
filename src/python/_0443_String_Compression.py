class Solution:
    def compress(self, chars: List[str]) -> int:
        turtle, idx = 0, 0

        for hare in range(1, len(chars) + 1):
            if hare < len(chars) and chars[turtle] == chars[hare]:
                continue

            count = hare - turtle
            chars[idx] = chars[turtle]
            idx += 1
            turtle = hare

            if count == 1:
                continue

            for digit in str(count):
                chars[idx] = digit
                idx += 1

        return idx

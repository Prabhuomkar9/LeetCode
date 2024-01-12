class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        limit = len(s) // 2
        multiplier = 1
        freq = 0

        for i, c in enumerate(s):
            if i == limit:
                multiplier = -1

            if c in "aAeEiIoOuU":
                freq += multiplier

        return freq == 0

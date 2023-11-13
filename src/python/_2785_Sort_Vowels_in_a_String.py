class Solution:
    def sortVowels(self, s: str) -> str:
        pq = []

        for _, c in enumerate(s):
            if c in {"A", "a", "E", "e", "I", "i", "O", "o", "U", "u"}:
                heappush(pq, c)

        s = list(s)

        for i, c in enumerate(s):
            if c in {"A", "a", "E", "e", "I", "i", "O", "o", "U", "u"}:
                s[i] = heappop(pq)

        return "".join(s)

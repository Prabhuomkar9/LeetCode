class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        freq = defaultdict(int)

        for word in words:
            for c in word:
                freq[c] += 1

        n = len(words)
        for v in set(freq.values()):
            if v % n != 0:
                return False

        return True

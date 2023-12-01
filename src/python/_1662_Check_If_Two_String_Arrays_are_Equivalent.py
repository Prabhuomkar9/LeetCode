class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        def gen(word):
            for fragment in word:
                for c in fragment:
                    yield c

        for c1, c2 in zip_longest(gen(word1), gen(word2)):
            if c1 != c2:
                return False

        return True

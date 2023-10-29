class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        seen1 = {c: word1.count(c) for c in set(word1)}
        seen2 = {c: word2.count(c) for c in set(word2)}

        if seen1.keys() != seen2.keys():
            return False

        freq1 = {f: list(seen1.values()).count(f) for f in seen1.values()}
        freq2 = {f: list(seen2.values()).count(f) for f in seen2.values()}

        if freq1 != freq2:
            return False

        return True

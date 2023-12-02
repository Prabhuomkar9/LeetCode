class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        freq = Counter(chars)

        for word in words:
            count = Counter(word)

            if all(freq[ch] >= count[ch] for ch in word):
                ans += len(word)

        return ans

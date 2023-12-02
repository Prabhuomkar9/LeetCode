class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        freq = defaultdict(int)

        for char in chars:
            freq[char] += 1

        for word in words:
            count = freq.copy()
            flag = False

            for char in word:
                count[char] -= 1
                if count[char] < 0:
                    flag = True
                    break

            if not flag:
                ans += len(word)

        return ans

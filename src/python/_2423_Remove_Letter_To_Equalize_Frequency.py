class Solution:
    def equalFrequency(self, word: str) -> bool:
        frequency = {}

        for letter in word:
            frequency[letter] = frequency.get(letter, 0) + 1

        for letter in word:
            frequency[letter] -= 1

            if frequency[letter] == 0:
                frequency.pop(letter)

            if len(set(frequency.values())) == 1:
                return True

            frequency[letter] = frequency.get(letter, 0) + 1

        return False

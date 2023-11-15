class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        setJ = set(jewels)

        return sum(s in setJ for s in stones)

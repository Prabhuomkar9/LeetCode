class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white = 0

        for i in range(k):
            white += blocks[i] == "W"

        ans = white

        for i in range(k, len(blocks)):
            white += blocks[i] == "W"
            white -= blocks[i - k] == "W"
            ans = min(ans, white)

        return ans

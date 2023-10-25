class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 1
        flowerbed = [0] + flowerbed + [0]

        while i < len(flowerbed) - 1:
            if flowerbed[i - 1] + flowerbed[i] + flowerbed[i + 1] == 0:
                n -= 1
                i += 1
            i += 1

        return n <= 0

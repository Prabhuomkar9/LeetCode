class Solution:
    def fullBloomFlowers(
        self, flowers: List[List[int]], people: List[int]
    ) -> List[int]:
        startsAt = sorted(flower[0] for flower in flowers)
        stopsAt = sorted(flower[1] for flower in flowers)

        ans = []

        for person in people:
            ans.append(bisect_right(startsAt, person) - bisect_left(stopsAt, person))

        return ans

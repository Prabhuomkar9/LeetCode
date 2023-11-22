class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        hashes = []
        total = 0

        for i, row in enumerate(nums):
            for j, num in enumerate(row):
                heapq.heappush(hashes, (i + j, len(nums) - i, num))
                total += 1

        ans = []
        for _ in range(total):
            ans.append(heapq.heappop(hashes)[2])

        return ans

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        ans = []

        for i, row in enumerate(nums):
            for j, num in enumerate(row):
                if len(ans) <= i + j:
                    ans.append([])
                ans[i + j].insert(0, num)

        return [num for row in ans for num in row]

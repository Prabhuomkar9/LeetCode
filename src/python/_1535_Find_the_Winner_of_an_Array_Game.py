class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        curr = arr[0]
        count = 0

        for i in range(1, len(arr)):
            if arr[i] > curr:
                curr = arr[i]
                count = 0

            count += 1

            if count == k:
                break

        return curr

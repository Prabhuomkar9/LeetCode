class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        currSum = sum(arr[:k])
        count = 0

        for i in range(k, len(arr) + 1):
            if currSum >= threshold * k:
                count += 1

            if i < len(arr):
                currSum += arr[i]

            currSum -= arr[i - k]

        return count

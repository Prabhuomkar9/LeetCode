class Solution:
    # def findSpecialInteger(self, arr: List[int]) -> int:
    #     freq = defaultdict(int)

    #     for num in arr:
    #         freq[num] += 1
    #         if freq[num] > len(arr) / 4:
    #             return num

    # def findSpecialInteger(self, arr: List[int]) -> int:
    #     interval = len(arr) // 4

    #     for i in range(len(arr) - interval):
    #         if arr[i] == arr[i + interval]:
    #             return arr[i]

    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        candidates = (arr[n // 4], arr[n // 2])

        for candidate in candidates:
            l, r = 0, n - 1

            while l <= r:
                m = l + (r - l) // 2

                if arr[m] >= candidate:
                    r = m - 1
                else:
                    l = m + 1

            right = arr[l + n // 4]

            if arr[l] == right:
                return candidate

        return arr[3 * n // 4]

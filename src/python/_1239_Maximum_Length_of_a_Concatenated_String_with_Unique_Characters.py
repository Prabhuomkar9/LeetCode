class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def dfs(i, seen):
            if i >= len(arr):
                return 0

            notIncluded = dfs(i + 1, seen)

            currSeen = set()
            for c in arr[i]:
                if c in seen or c in currSeen:
                    return notIncluded
                currSeen.add(c)

            included = len(arr[i]) + dfs(i + 1, seen | set(arr[i]))

            return max(notIncluded, included)

        return dfs(0, set())

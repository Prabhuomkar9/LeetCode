class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)

        seen = set()

        for key in count:
            if count[key] in seen:
                return False
            else:
                seen.add(count[key])

        return True

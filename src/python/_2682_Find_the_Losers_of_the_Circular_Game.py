class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        seen = set()
        i = 1
        num = 0

        while num not in seen:
            seen.add(num)
            num += i * k
            num %= n
            i += 1

        ans = []

        for num in range(n):
            if num not in seen:
                ans.append(num + 1)

        return ans

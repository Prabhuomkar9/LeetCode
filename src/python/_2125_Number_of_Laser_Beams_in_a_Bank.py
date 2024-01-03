class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = 0
        ans = 0

        for row in bank:
            curr = row.count('1')
            if curr != 0:
                ans += prev * curr
                prev = curr

        return ans

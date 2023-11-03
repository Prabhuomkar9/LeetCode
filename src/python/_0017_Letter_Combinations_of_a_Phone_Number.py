class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        buttons = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        ans = []

        def dfs(s, idx):
            if idx >= len(digits):
                ans.append(s)
                return

            for c in buttons[digits[idx]]:
                dfs(s + c, idx + 1)

        dfs("", 0)

        return ans

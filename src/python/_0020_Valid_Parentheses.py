class Solution:
    def isValid(self, s: str) -> bool:
        pair = {"(": ")", "{": "}", "[": "]"}

        seen = []

        for st in s:
            if st in pair:
                seen.append(st)
            else:
                if not seen or st != pair[seen.pop()]:
                    return False

        if seen:
            return False

        return True

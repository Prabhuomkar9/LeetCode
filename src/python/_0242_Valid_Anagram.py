class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = {}
        for c in s:
            seen[c] = seen[c] + 1 if c in seen else 1
        for c in t:
            if c not in seen:
                return False
            seen[c] -= 1
            if seen[c] == -1:
                return False
        return True

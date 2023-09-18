class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for s in strs:
            hashS = "".join(sorted(s))

            if hashS in result:
                result[hashS].append(s)
            else:
                result[hashS] = [s]

        return result.values()

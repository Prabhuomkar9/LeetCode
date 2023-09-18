class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = set()
        for val in nums:
            if val in hash:
                return True
            hash.add(val)
        return False

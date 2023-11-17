class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()

        return max(nums[i] + nums[-1 -i] for i in range(len(nums) // 2))

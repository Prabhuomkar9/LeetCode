class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        op = 0
        curr = nums[0]

        for num in nums:
            if curr != num:
                op += 1
                curr = num
            ans += op

        return ans

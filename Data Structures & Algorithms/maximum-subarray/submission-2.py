class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum = nums[0]
        best = nums[0]

        for i in range(1, len(nums)):
            currentSum = max(currentSum + nums[i], nums[i])
            best = max(best, currentSum)

        return best
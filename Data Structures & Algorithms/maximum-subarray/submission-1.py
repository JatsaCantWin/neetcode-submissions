class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = nums[0]
        curMax = nums[0]

        for num in nums[1:]:
            curSum = max(num, curSum + num)
            curMax = max(curMax, curSum)

        return curMax
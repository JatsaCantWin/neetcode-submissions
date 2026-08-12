class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curMax = 0
        curSum = 0

        allNegative = True

        for num in nums:
            if num >= 0:
                allNegative = False

            curSum += num
            if curSum < 0:
                curSum = 0
            curMax = max(curSum, curMax)
        
        if allNegative:
            curMax = max(nums)

        return curMax
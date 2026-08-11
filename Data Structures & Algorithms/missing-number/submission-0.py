class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expectedSum = 0
        actualSum = 0

        for i, num in enumerate(nums):
            expectedSum += i + 1
            actualSum += num

        return expectedSum - actualSum
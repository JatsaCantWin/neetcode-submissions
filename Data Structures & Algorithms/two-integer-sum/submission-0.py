class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        missingNumber = {}

        for i, num in enumerate(nums):
            if num in missingNumber:
                return [missingNumber[num][1], i]
    
            missingNumber[target - num] = (num, i)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            missingNum = target - num
            
            j = i + 1

            while j < len(numbers) and numbers[j] <= missingNum:
                if numbers[j] == missingNum:
                    return [i + 1, j + 1]
                j += 1
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        leftIndex = 0
        rightIndex = n - 1

        while leftIndex < rightIndex:
            missingNum = target - numbers[leftIndex]

            while numbers[rightIndex] >= missingNum:
                if numbers[rightIndex] == missingNum:
                    return [leftIndex +1, rightIndex +1]
                
                rightIndex -= 1
            
            leftIndex += 1
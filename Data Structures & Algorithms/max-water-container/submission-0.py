class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        leftIndex = 0
        rightIndex = n - 1

        maxContainerSize = 0

        while leftIndex < rightIndex:
            containerSize = (rightIndex - leftIndex) * min(heights[leftIndex], heights[rightIndex])
            maxContainerSize = max(maxContainerSize, containerSize)

            if heights[leftIndex] < heights[rightIndex]:
                leftIndex += 1
            else:
                rightIndex -= 1

        return maxContainerSize
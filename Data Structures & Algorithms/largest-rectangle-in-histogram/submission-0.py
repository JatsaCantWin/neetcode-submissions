class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        result = 0
        stack = []

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                result = max(result, height * (i - index))
                start = index

            stack.append((start, h))

        while stack:
            index, height = stack.pop()
            result = max(result, height * (len(heights) - index))

        return result
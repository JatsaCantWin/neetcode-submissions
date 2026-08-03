class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        height = len(matrix)
        width = len(matrix[0])

        n = height * width

        def getElement(i):
            return matrix[i // width][i % width]

        left = 0
        right = n - 1

        while left <= right:
            mid = (left + right) // 2

            if getElement(mid) == target:
                return True
            elif getElement(mid) < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
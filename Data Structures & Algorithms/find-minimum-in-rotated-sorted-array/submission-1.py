class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        def exploreWindow(left, right):
            mid = (left + right) // 2

            if mid == n - 1:
                return None

            if left > right:
                return None

            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]

            if left == right:
                return None
            
            exploreLeft = exploreWindow(left, mid - 1)
            exploreRight = exploreWindow(mid + 1, right)

            if exploreLeft is not None:
                return exploreLeft
            if exploreRight is not None:
                return exploreRight
        
        exploreNums = exploreWindow(0, n-1)

        if exploreNums is not None:
            return exploreNums
        else:
            return nums[0]
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        def exploreWindow(left, right):
            mid = (left + right) // 2

            if left > right:
                return None

            if nums[mid] == target:
                return mid
            
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
            return -1
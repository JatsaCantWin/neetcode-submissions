class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
                return None
        if n <= 3:
            return max(nums)

        def house_robber(nums):
            n = len(nums)

            nums[2] = nums[2] + nums[0]

            for i in range(3, n):
                nums[i] = nums[i] + max(nums[i-2], nums[i-3])
            
            return max(nums[n-1], nums[n-2])

        house_robber1 = house_robber(nums[1:])
        house_robber2 = house_robber(nums[:n-1])

        return max(house_robber1, house_robber2)
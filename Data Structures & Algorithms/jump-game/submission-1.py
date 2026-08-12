class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        maxJump = 0

        for i in range(n):
            if maxJump < i:
                return False
            if maxJump >= n - 1:
                return True
            
            maxJump = max(i + nums[i], maxJump)
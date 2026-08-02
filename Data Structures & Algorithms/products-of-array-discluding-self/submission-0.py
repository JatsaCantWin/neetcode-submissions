class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        if n == 1:
            return [1]

        prefixProduct = {}
        postfixProduct = {}

        prefixProduct[0] = nums[0]

        for i in range(1, n):
            prefixProduct[i] = prefixProduct[i - 1] * nums[i]

        postfixProduct[n - 1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            postfixProduct[i] = postfixProduct[i + 1] * nums[i]

        result = [0] * n

        for i in range(n):
            if i == 0:
                result[i] = postfixProduct[1]
            elif i == n - 1:
                result[i] = prefixProduct[n - 2]
            else:
                result[i] = (
                    prefixProduct[i - 1] *
                    postfixProduct[i + 1]
                )

        return result
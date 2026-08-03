class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        result = []

        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))

        result.append(-heap[0][0])

        for i in range(k, len(nums)):
            heapq.heappush(heap, (-nums[i], i))

            while heap[0][1] <= i - k:
                heapq.heappop(heap)

            result.append(-heap[0][0])

        return result
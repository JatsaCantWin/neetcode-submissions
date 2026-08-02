class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqueNums = set(nums)
        maxSequenceLength = 0

        for num in uniqueNums:
            if num - 1 not in uniqueNums:
                sequenceLength = 1
            
                while (num + sequenceLength) in uniqueNums:
                    sequenceLength += 1

                maxSequenceLength = max(sequenceLength, maxSequenceLength)

        return maxSequenceLength
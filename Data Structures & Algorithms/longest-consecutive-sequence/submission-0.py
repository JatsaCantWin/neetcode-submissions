class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequenceLengthByElement = {}
        maxSequenceLength = 0

        for num in nums:
            if num in sequenceLengthByElement:
                continue

            sequenceLengthByElement[num] = 1
            sequenceLengthToTheRight = 0
            sequenceLengthToTheLeft = 0

            if num + 1 in sequenceLengthByElement:
                sequenceLengthToTheRight = sequenceLengthByElement[num + 1]
            
            if num - 1 in sequenceLengthByElement:
                sequenceLengthToTheLeft = sequenceLengthByElement[num - 1]

            sequenceLengthByElement[num] += sequenceLengthToTheRight
            sequenceLengthByElement[num] += sequenceLengthToTheLeft

            sequenceLengthByElement[num + sequenceLengthToTheRight] = sequenceLengthByElement[num]
            sequenceLengthByElement[num - sequenceLengthToTheLeft] = sequenceLengthByElement[num]

            if sequenceLengthByElement[num] > maxSequenceLength:
                maxSequenceLength = sequenceLengthByElement[num]

        return maxSequenceLength
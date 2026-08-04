class TimeMap:

    def __init__(self):
        self.memory = {} # [(timestamp, value)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.memory:
            self.memory[key] = []

        self.memory[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.memory:
            return ""

        timeline = self.memory[key]

        n = len(timeline)
        left = 0
        right = n -1

        ans = ""

        while left <= right:
            mid = (left + right) // 2

            if timeline[mid][0] <= timestamp:
                ans = timeline[mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return ans
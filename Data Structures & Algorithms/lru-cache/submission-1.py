class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.removalQueue = deque()
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.removalQueue.remove(key)
        self.removalQueue.append(key)

        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.removalQueue.remove(key)
            self.removalQueue.append(key)
            return

        if len(self.cache) >= self.capacity:
            removedElement = self.removalQueue.popleft()
            self.cache.pop(removedElement)
        
        self.cache[key] = value
        self.removalQueue.append(key)
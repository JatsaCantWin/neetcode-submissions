class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        result = n
        stack = []
        cars = [[position[i], speed[i]] for i in range(n)]
        cars.sort()
        carArrival = [(target - cars[i][0]) / cars[i][1] for i in range(n)]

        for car in range(n-1, -1, -1):
            stack.append(carArrival[car])

            if len(stack) > 1:
                if stack[-1] <= stack[-2]:
                    stack.pop()
                    result -= 1
        
        return result
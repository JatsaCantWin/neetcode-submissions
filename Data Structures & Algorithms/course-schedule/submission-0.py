class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)

        state = [0] * numCourses

        def dfs(course):
            if state[course] == 1:
                return False  # cycle

            if state[course] == 2:
                return True   # already completely explored

            state[course] = 1

            for nextCourse in graph[course]:
                if not dfs(nextCourse):
                    return False

            state[course] = 2
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True

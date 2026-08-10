class Solution:
    def foreignDictionary(self, words: list[str]) -> str:
        graph = {c: set() for word in words for c in word}
        indegree = {c: 0 for c in graph}

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if c2 not in graph[c1]:
                        graph[c1].add(c2)
                        indegree[c2] += 1
                    break

        q = deque(c for c in graph if indegree[c] == 0)

        order = []

        while q:
            c = q.popleft()
            order.append(c)

            for nxt in graph[c]:
                indegree[nxt] -= 1

                if indegree[nxt] == 0:
                    q.append(nxt)

        if len(order) != len(graph):
            return ""

        return "".join(order)
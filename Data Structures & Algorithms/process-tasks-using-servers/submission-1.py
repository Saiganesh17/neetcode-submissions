import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        available = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(available)

        busy = []  # (finish_time, weight, index)
        res = []

        time = 0

        for t, duration in enumerate(tasks):
            time = max(time, t)

            # Release all servers that have finished
            while busy and busy[0][0] <= time:
                finish, weight, idx = heapq.heappop(busy)
                heapq.heappush(available, (weight, idx))

            # Wait until a server becomes available
            if not available:
                time = busy[0][0]

                while busy and busy[0][0] <= time:
                    finish, weight, idx = heapq.heappop(busy)
                    heapq.heappush(available, (weight, idx))

            weight, idx = heapq.heappop(available)
            res.append(idx)

            heapq.heappush(busy, (time + duration, weight, idx))

        return res
        #time and space is O((n+m)* logn) and O(n) respectively
"""
You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.
"""

"""
Intuition:
For each stop, first add the bus into a dictionary where the stop is the key and the bus is the element added into a list. Then we create a bfs queue with the source. We add all of the busses that take the source bus stop into the queue and do a bfs and go on until we
find the target bus stop. Return the number of stops it took to get to the bus stop."""
from collections import deque
from collections import defaultdict
class Solution:
    def numBusesToDestination(self, routes, source: int, target: int) -> int:
        g = defaultdict(list)
        for i, stops in enumerate(routes):
            for stop in stops:
                g[stop].append(i)
        
        q = deque([source])
        sol = 0
        visited = set()
        while q:
            for _ in range(len(q)):
                stop = q.popleft()
                if stop == target:
                    return sol
                for bus in g[stop]:
                    if bus not in visited:
                        visited.add(bus)
                        q.extend(routes[bus])
            sol +=1
        return -1

s = Solution()
s.numBusesToDestination(routes = [[1,2,7],[3,6,7]], source = 1, target = 6)
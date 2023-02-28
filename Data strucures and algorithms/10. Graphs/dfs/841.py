"""
There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.
"""
"""
Intuition:
Create a visited set and do a dfs through the keys in the rooms starting with room 0. If all the rooms are visited we know the solution is true. Else false.
"""
class Solution:
    def canVisitAllRooms(self, rooms) -> bool:
        def dfs(i):
            for key in rooms[i]:
                if key not in visited:
                    visited.add(key)
                    dfs(key)
        
        visited = {0}
        dfs(0)
        return True if len(visited) == len(rooms) else False
        
s = Solution()
s.canVisitAllRooms(rooms = [[1],[2],[3],[]])
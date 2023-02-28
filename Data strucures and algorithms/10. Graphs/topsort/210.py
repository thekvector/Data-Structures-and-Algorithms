"""There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
"""
"""
Intuition:
Use a topological sort to check for the courses. Any course can be taken once its pre requisite courses have been taken. We can visit a node when all of its previously connected nodes are visited.
"""
from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, pre):
        g = defaultdict(list)
        for u,v in pre:
            g[v].append(u)
        
        def dfs(i, stack):
            for j in g[i]:
                if j not in visited:
                    visited.add(j)
                    stack.add(j)
                    if not dfs(j,stack):
                        return False
                    stack.remove(j)
                if j in stack:
                    return False
            self.sol = [i] + self.sol
            return True
        
        visited = set()
        self.sol = []
        for i in range(numCourses):
            if i not in visited:
                visited.add(i)
                if not dfs(i,{i}):
                    return []
        return self.sol

s = Solution()
s.findOrder(4,[[1,0],[2,0],[3,1],[3,2]])
"""
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).
"""
"""
Intuition:
Do a dfs through the adjacency list to find all of the paths using a current list. """
class Solution:
    def allPathsSourceTarget(self, graph):
        n = len(graph)
        def dfs(i, cur):
            if i == n-1:
                sol.append(cur[:])
                return
            for j in graph[i]:
                cur.append(j)
                dfs(j,cur)
                del cur[-1]
        
        sol = []
        dfs(0, [0])
        return sol

s = Solution()
s.allPathsSourceTarget( graph = [[1,2],[3],[3],[]])
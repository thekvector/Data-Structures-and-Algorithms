"""
You are given an n x n integer matrix board where the cells are labeled from 1 to n2 in a Boustrophedon style starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.

You start on square 1 of the board. In each move, starting from square curr, do the following:

Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n2)].
This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations, regardless of the size of the board.
If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.
The game ends when you reach the square n2.
A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or ladder is board[r][c]. Squares 1 and n2 do not have a snake or ladder.

Note that you only take a snake or ladder at most once per move. If the destination to a snake or ladder is the start of another snake or ladder, you do not follow the subsequent snake or ladder.

For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2. You follow the ladder to square 3, but do not follow the subsequent ladder to 4.
Return the least number of moves required to reach the square n2. If it is not possible to reach the square, return -1."""

"""
Intuition:
First iterate through the matrix and find all of the snakes and ladder and put it into a hashmap. Then create a queue for the breadth first search. We add to the queues all of the values betweeen the current value + 6 because we can roll any number between 1 and 6.
If the position we reach eer equals n*n we know we have to reached the end and we can return the number of turns it took to get there.
"""

from collections import defaultdict
from collections import deque
class Solution:
    def snakesAndLadders(self, board) -> int:
        sl = defaultdict(int)
        pos = 1
        n = len(board)
        flag = 1
        for i in range(n-1,-1,-1):
            if flag >0:
                for j in range(n):
                    if board[i][j] != -1:
                        sl[pos] = board[i][j]
                    pos+=1
                flag*= -1
            else:
                for j in range(n-1,-1, -1):
                    if board[i][j] != -1:
                        sl[pos] = board[i][j] 
                    pos+=1
                flag*=-1
        
        visited = [0 for i in range(n*n)]
        q = deque([(1,0)])
        while q:
            pos, steps = q.popleft()
            dice = min(pos +6, n*n)
            for i in range(pos+1, dice +1):
                stop = i
                if stop in sl:
                    stop = sl[stop]
                if stop == n*n:
                    return steps + 1
                if visited[stop] == 0:
                    q.append((stop,steps + 1))
                    visited[stop] = 1
        
        return -1

s = Solution()
s.snakesAndLadders([[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]])
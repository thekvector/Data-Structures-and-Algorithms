"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.
"""

"""
Intuition: We want to create a graph with every word in the wordList. With the word, we want to iterate through the letters and replace the letter of the current iteration with a star and add that to the graph with the original word being the element that is added
into the list. Then we create a bfs qeueue with the beginWord in the queue. We loop through the words in the queue and replace each letter of the word with a star and find the words that are associated with the star replaced words until we reach endWord. Return 
the number of steps it took to get to the endWord.
"""

from collections import defaultdict
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        n = len(endWord)
        g = defaultdict(list)
        for word in wordList:
            for i in range(n):
                w = word[:i] + "*" + word[i+1:]
                g[w].append(word)
        q = deque([beginWord])
        visited = set()
        sol = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                for i in range(n):
                    w = word[:i] + "*" +word[i+1:]
                    for j in g[w]:
                        if j not in visited:
                            if j == endWord:
                                return sol + 1
                            visited.add(j)
                            q.append(j)
            sol+=1
        return 0

s = Solution()
s.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"])
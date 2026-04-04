from collections import deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        q=deque()
        word_list=set(wordList)
        q.append((beginWord,1))

        if endWord not in word_list: return 0

        while q:

            word,step=q.popleft()

            if word==endWord: return step

            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new= word[:i] + c + word[i+1:]

                    if new in word_list:
                        word_list.remove(new)
                        q.append((new,step+1))
                
        return 0

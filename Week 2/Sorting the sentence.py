class Solution:
    def sortSentence(self, s: str) -> str:
        postion = {}
        for i in range (len(s.split(' '))):
            postion[s.split(' ')[i][-1]] = s.split(' ')[i][:-1]
        return (' '.join([postion[str(i)] for i in range(1, len(s.split(' '))+1)]))
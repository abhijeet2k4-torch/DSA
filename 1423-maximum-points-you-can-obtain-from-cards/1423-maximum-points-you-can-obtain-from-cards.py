class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        maxscore = 0
        counter = 0
        for i in range(k+1):
            if maxscore == 0:
                for n in cardPoints[-k:]:
                    counter += n
                if k == len(cardPoints):
                    return counter
            else:
                counter -= cardPoints[-k+i-1] - cardPoints[i-1]
            maxscore = max(maxscore,counter)
        return maxscore

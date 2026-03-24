from collections import Counter

class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        # if (len(hand)%groupSize==0): return True

        # return False
        hand.sort()

        freq=Counter(hand)

        for num in hand:
            if freq[num]>0:
                for i in range(groupSize):
                    if freq[num+i]<=0: return False
                    else:
                        freq[num+i]-=1

        return True
        
        

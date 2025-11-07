from typing import List
from collections import defaultdict

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()

        needed = defaultdict(lambda: 0)
        card_set = set(hand)

        # greedy. sort and walk
        # can probably do this more mathematicly with a multiset, but let's do it iteratively with a linear scan
        for card in hand:
            if needed[card]:
                needed[card] -= 1
            else:
                for i in range(1, groupSize):
                    needed[card + i] += 1
                    if card + i not in card_set:
                        return False # prevent mem from exceeding `len(hand)`

        return sum(needed.values()) == 0
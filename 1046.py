from heapq import heappush, heappop, heapify
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones] # have to negate for max heap (would use *_max functions if py version were newer)
        heapify(stones)

        while len(stones) > 1:
            (a, b) = -heappop(stones), -heappop(stones)
            if a - b != 0:
                heappush(stones, -(a - b))

        return -stones[0] if stones else 0
from typing import List

class Solution:
    """
    # backtracking solution

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 1:
            return 0
        else:
            return min(cost[0] + self.minCostClimbingStairs(cost[1:]), cost[1] + self.minCostClimbingStairs(cost[2:]))
    """

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost_to_climb_from: List[int] = [0] * (2 + len(cost)) # 2 trailling zeroes as sentinel values

        for i in reversed(range(len(cost))):
            cost_to_climb_from[i] = cost[i] + min(cost_to_climb_from[i + 1], cost_to_climb_from[i + 2])

        return min(cost_to_climb_from[0:2])

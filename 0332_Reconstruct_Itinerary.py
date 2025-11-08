from typing import List
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # greedy graph traversal

        # use adjacency dict instead of adjacency list to get ordered multiset
        cnx = defaultdict(lambda: defaultdict(int)) # [airport_from] -> ([airport_to] -> count)

        for (frum, to) in sorted(tickets):
            cnx[frum][to] += 1

        def min_lex_traverse(start: str) -> List[str]:
            curr = start
            res = [start]

            while cnx[curr]:
                to = next(iter(cnx[curr]))
                cnx[curr][to] -= 1

                if cnx[curr][to] == 0:
                    del cnx[curr][to]

                res.append(to)
                curr = to

            return res

        res = min_lex_traverse("JFK")

        # now we have reached a dead-end (we know res[0] is the correct start and res[-1] must be the correct
        # end node because they both have indegree != outdegree)
        # it is possible, however, that not all edges are being used
        # but since we know that there exists a path that uses all edges, this implies that
        # the graph formed by the remaining edges must only contain nodes of matching indegree and outdegree
        # (w/r/t the remaining edges)
        # => all remaining nodes are part of cycles (which can be traversed greedily w/o the concern of reaching a dead-end)
        # we must add these cycles to `res`, however, by definition, `res` is already at a lexicographical minimum
        # and we expicitly made each choice in `res` accordingly, therefore all new cycles should
        # begrudglingly added as far back in `res` as possible.
        # using the same greedy algorithm

        def rec(old):
            # assemble `old` backwards, populating cycles
            old2_reversed = []

            for airport in reversed(old):
                cycle = min_lex_traverse(airport)
                if len(cycle) > 1:
                    cycle2 = rec(cycle)
                    old2_reversed += reversed(cycle2)
                else:
                    old2_reversed += reversed(cycle)

            return list(reversed(old2_reversed))

        return rec(res)

        # this solution is slop, but I'll leave it
        # I realize it probably could be implemented with a single recursive dfs
        # but it took a while to get this far
        # this one's pretty tricky from scratch because it's both:
        # 1. Eulerian Path Finding
        # 2. Realization that lexicographical reverse-assembly will work
        # considerably easier if you have either or both of those fresh in your mind, but
        # when cold, it's a bit wicked
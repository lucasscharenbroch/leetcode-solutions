from typing import List
from queue import PriorityQueue
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        vis = set()
        distance_map = {k: 0} # [node] -> dist
        cnx = defaultdict(list) # [node] -> [(neigh, weight)]

        # build adj list
        for (u, v, w) in times:
            cnx[u].append((v, w))

        # dijkstras
        q = PriorityQueue()
        q.put((0, k))

        while not q.empty():
            (dist, node) = q.get()
            if node in vis:
                continue
            vis.add(node)
            distance_map[node] = dist

            for (neigh, dneigh) in cnx[node]:
                if not neigh in vis:
                    q.put((dist + dneigh, neigh))

        return max(distance_map.values()) if len(vis) == n else -1
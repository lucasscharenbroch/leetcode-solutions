class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        copied_nodes_dict = {} # [val] -> node

        # recursive (I much perfer)
        # def recursive_copy(node: 'Node') -> 'Node':
        #     if node.val in copied_nodes_dict:
        #         return copied_nodes_dict[node.val]

        #     copy = Node(node.val)
        #     copied_nodes_dict[node.val] = copy

        #     copy.neighbors = [recursive_copy(n) for n in node.neighbors]
        #     return copy

        # return recursive_copy(node)

        # iterative
        vis = {node}
        q = [node]
        copied_nodes_dict[node.val] = Node(node.val)
        while q:
            top = q.pop(0)
            q += list(set(top.neighbors) - vis)
            vis |= set(top.neighbors)

            for n in top.neighbors:
                if n.val not in copied_nodes_dict:
                    copied_nodes_dict[n.val] = Node(n.val)

            copied_nodes_dict[top.val].neighbors = [copied_nodes_dict[n.val] for n in top.neighbors]
        return copied_nodes_dict[node.val]

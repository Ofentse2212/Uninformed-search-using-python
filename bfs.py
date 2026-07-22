"""Breadth-first traversal for an adjacency-list graph."""

from collections import deque


def bfs(graph, start):
    """Return nodes in breadth-first order from *start*."""
    if start not in graph:
        raise ValueError(f"Unknown start node: {start}")

    order = []
    visited = {start}
    queue = deque([start])

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order

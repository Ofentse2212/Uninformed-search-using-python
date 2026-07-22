"""Depth-first traversal for an adjacency-list graph."""


def dfs(graph, start):
    """Return nodes in deterministic depth-first order from *start*."""
    if start not in graph:
        raise ValueError(f"Unknown start node: {start}")

    order = []
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node in visited:
            continue

        visited.add(node)
        order.append(node)
        stack.extend(
            neighbor
            for neighbor in reversed(graph.get(node, []))
            if neighbor not in visited
        )

    return order

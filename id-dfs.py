"""Iterative-deepening depth-first search."""


def depth_limited_search(graph, node, depth_limit, visited):
    """Visit reachable nodes without exploring beyond *depth_limit*."""
    if depth_limit < 0 or node in visited:
        return

    visited.append(node)
    if depth_limit == 0:
        return

    for neighbor in graph.get(node, []):
        depth_limited_search(graph, neighbor, depth_limit - 1, visited)


def iddfs(graph, start, max_depth):
    """Return the traversal produced at every depth from zero to max_depth."""
    if start not in graph:
        raise ValueError(f"Unknown start node: {start}")
    if max_depth < 0:
        raise ValueError("max_depth must be non-negative")

    result = {}
    for depth in range(max_depth + 1):
        visited = []
        depth_limited_search(graph, start, depth, visited)
        result[depth] = visited

    return result

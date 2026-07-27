# Uninformed Search Algorithms in Python

A small, visual introduction to three foundational graph-search strategies: breadth-first search (BFS), depth-first search (DFS) and iterative-deepening DFS (IDDFS).

This project began as an AI practical, but its purpose is broader than producing three traversals. It makes the behaviour and trade-offs of each algorithm easier to inspect, test and explain—skills that also support route planning, recommendation systems and other socially useful applications.

## Algorithms

| Algorithm | Main idea | Useful when |
|---|---|---|
| BFS | Explores one level at a time | The shallowest unweighted solution is required |
| DFS | Explores one path before backtracking | Memory is limited or deep exploration is useful |
| IDDFS | Repeats DFS with increasing limits | Depth is unknown and BFS-like completeness is needed |

## Run the project

```bash
python uninformed_test.py
```

The script uses Python's built-in `unittest` module, so no test dependency is required.

To display the graph used in the original practical, install the optional visualisation packages:

```bash
pip install networkx matplotlib
```

## Example graph

```text
        A
      /   \
     B     C
    / \     \
   D   E     F
       |
       G
```

Expected traversal from `A`:

- BFS: `A, B, C, D, E, F, G`
- DFS: `A, B, D, E, G, C, F`
- IDDFS: shows how the reachable set grows at every depth limit

## Improvements in this version

- Removed accidental shell-command wrappers from the Python files
- Added input validation and deterministic traversal
- Replaced repeated list membership checks with sets where appropriate
- Added regression tests for all three algorithms
- Documented the algorithms and their practical trade-offs

## Author

Built by Ofentse Seko while developing a portfolio in applied AI and purposeful software.

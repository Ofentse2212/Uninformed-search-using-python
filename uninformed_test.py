"""Executable demonstration and regression tests for the search algorithms."""

import importlib
import unittest

from bfs import bfs
from dfs import dfs

iddfs = importlib.import_module("id-dfs").iddfs

GRAPH = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": [],
}


class SearchAlgorithmTests(unittest.TestCase):
    def test_bfs_visits_level_by_level(self):
        self.assertEqual(bfs(GRAPH, "A"), ["A", "B", "C", "D", "E", "F", "G"])

    def test_dfs_is_deterministic(self):
        self.assertEqual(dfs(GRAPH, "A"), ["A", "B", "D", "E", "G", "C", "F"])

    def test_iddfs_expands_the_depth_limit(self):
        self.assertEqual(iddfs(GRAPH, "A", 2)[2], ["A", "B", "D", "E", "C", "F"])

    def test_unknown_start_is_rejected(self):
        with self.assertRaises(ValueError):
            bfs(GRAPH, "Z")


if __name__ == "__main__":
    unittest.main(verbosity=2)

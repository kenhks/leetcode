from collections import defaultdict
from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    BFS, Use hashmap to store node to the set of adjacent node
    Time Complexity: O(V + E) = V + 2E
    Space Complexity: O(V + E) = 2V + E
    V = the number of vertice
    E = the number of edge
    """

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        graph = {}
        for u, v in edges:
            if u in graph:
                graph[u].add(v)
            else:
                graph[u] = set([v])
            if v in graph:
                graph[v].add(u)
            else:
                graph[v] = set([u])
        valid = False
        if source in graph:
            next_vertices = graph[source]
            visited_vertices = set()
            while len(next_vertices) > 0:
                new_next_vertices = set()
                for v in next_vertices:
                    if v == destination:
                        valid = True
                        break
                    if v in graph and v not in visited_vertices:
                        new_next_vertices |= graph[v]
                    visited_vertices.add(v)
                if valid:
                    break
                next_vertices = new_next_vertices
        return valid


class Solution2:
    """
    DFS, Use hashmap to store node to the set of adjacent node
    Time Complexity: O(V + E) = V + 2E
    Space Complexity: O(V + E) = 2V + E
    V = the number of vertice
    E = the number of edge
    """

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        graph = defaultdict(set)
        for u, v in edges:
            if u in graph:
                graph[u].add(v)
            else:
                graph[u] = set([v])
            if v in graph:
                graph[v].add(u)
            else:
                graph[v] = set([u])
        valid = False
        visited_vertices = set()

        def dfs(v):
            nonlocal valid
            nonlocal visited_vertices
            if v == destination:
                valid = True
            elif v not in visited_vertices:
                visited_vertices.add(v)
                for next_v in graph[v]:
                    dfs(next_v)
                    if valid:
                        break

        dfs(source)
        return valid


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "validPath",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    n = 3
    edges = [[0, 1], [1, 2], [2, 0]]
    assert solution(n, edges, source=0, destination=2)


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    n = 6
    edges = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
    assert not solution(n, edges, source=0, destination=5)


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    n = 1
    edges = []
    assert solution(n, edges, source=0, destination=0)


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    n = 2
    edges = [(1, 2)]
    assert not solution(n, edges, source=0, destination=1)

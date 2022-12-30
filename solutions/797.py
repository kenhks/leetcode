from collections import deque
from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    DFS, Iterative
    Time Complexity: O(n^2)
    Space Complexity: O(n^2)
    """

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        stack = deque([[0]])
        n = len(graph) - 1
        while stack:
            for _ in range(len(stack)):
                path = stack.popleft()
                if path[-1] == n:
                    ans.append(path)
                else:
                    for node in graph[path[-1]]:
                        stack.append(path + [node])
        return ans


class Solution2:
    """
    DFS, Recursive
    Time Complexity: O(n^2)
    Space Complexity: O(n^2)
    n = the number of node in graph
    """

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        n = len(graph) - 1

        def dfs(path):
            if path[-1] == n:
                ans.append(path)
            else:
                for node in graph[path[-1]]:
                    dfs(path + [node])

        dfs([0])
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "allPathsSourceTarget",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    graph = [[1, 2], [3], [3], []]
    expected = [[0, 1, 3], [0, 2, 3]]
    assert set(tuple(i) for i in solution(graph)) == set(tuple(i) for i in expected)


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
    expected = [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]
    assert set(tuple(i) for i in solution(graph)) == set(tuple(i) for i in expected)

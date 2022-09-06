from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Graph Theory
    Time Complexity: O(V + E)
    Space Complexity: O(V)
    V = n = the number of vertices
    E = length of trust = the number of edges
    """

    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust:
            return 1 if n == 1 else -1
        degrees = [0] * (n + 1)
        for a, b in trust:
            degrees[a] -= 1
            degrees[b] += 1
        for i in range(1, n + 1):
            if degrees[i] == n - 1:
                return i
        else:
            return -1


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "findJudge",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    trust = [[1, 2]]
    assert solution(2, trust) == 2


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    trust = [[1, 3], [2, 3]]
    assert solution(3, trust) == 3


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    trust = [[1, 3], [2, 3], [3, 1]]
    assert solution(3, trust) == -1

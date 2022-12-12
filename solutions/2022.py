from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Time Complexity: O(mn)
    Space Complexity: O(mn)
    """

    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        size = m * n
        if len(original) != size:
            return []
        return [original[i : i + n] for i in range(0, size, n)]


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "construct2DArray",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(original=[1, 2, 3, 4], m=2, n=2) == [[1, 2], [3, 4]]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(original=[1, 2, 3], m=1, n=3) == [[1, 2, 3]]


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(original=[1, 2], m=1, n=1) == []


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert solution(original=[1], m=1, n=1) == [[1]]

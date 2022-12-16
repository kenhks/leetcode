from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Hashset
    Time Complexity: O(mn) = 2mn
    Space Complexity: O(m + n)
    """

    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        row_min = set(min(row) for row in matrix)
        col_max = set(max(col) for col in zip(*matrix))
        return list(row_min & col_max)


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "luckyNumbers",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    matrix = [
        [3, 7, 8],
        [9, 11, 13],
        [15, 16, 17],
    ]
    assert solution(matrix) == [15]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    matrix = [
        [1, 10, 4, 2],
        [9, 3, 8, 7],
        [15, 16, 17, 12],
    ]
    assert solution(matrix) == [12]


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    matrix = [
        [7, 8],
        [1, 2],
    ]
    assert solution(matrix) == [7]

from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Append element one by one
    Time Complexity: O(mn)
    Space Complexity: O(mn)
    """

    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if r * c != m * n:
            return mat
        row = []
        new_mat = []
        for i in range(m):
            for j in range(n):
                if len(row) < c:
                    row.append(mat[i][j])
                if len(row) == c:
                    new_mat.append(row)
                    row = []
        return new_mat


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "matrixReshape",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    mat = [
        [1, 2],
        [3, 4],
    ]
    assert solution(mat, r=1, c=4) == [[1, 2, 3, 4]]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    mat = [
        [1, 2],
        [3, 4],
    ]
    assert solution(mat, r=2, c=4) == [[1, 2], [3, 4]]

from heapq import nsmallest
from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Python built-in sum and sort
    Time Complexity: O(mn) = mn + mlog(2, m)
    Space Complexity: O(m) = 2m
    m = len(mat), n = len(mat[0])
    """

    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        data = [(i, sum(row)) for i, row in enumerate(mat)]
        data.sort(key=lambda x: x[1])
        return [i[0] for i in data[:k]]


class Solution2:
    """
    Binary search on row and heapify result
    Time Complexity: O(mlog(2, n)) = mlog(2, n)
    Space Complexity: O(m) = 2m
    m = len(mat), n = len(mat[0])
    """

    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        def search(row_data):
            i, row = row_data
            if row[0] == 0:
                return i, 0
            elif row[-1] == 1:
                return i, len(row)
            else:
                ans = -1
                left, right = 0, len(row) - 1
                while left <= right:
                    mid = left + (right - left) // 2
                    if row[mid] == 1:
                        ans = mid
                        left = mid + 1
                    else:
                        right = mid - 1
                return i, ans + 1

        return [i[0] for i in nsmallest(k, map(search, enumerate(mat)), key=lambda x: x[1])]


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "kWeakestRows",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    matrix = [
        [1, 1, 0, 0, 0],
        [1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [1, 1, 1, 1, 1],
    ]
    assert solution(matrix, k=3) == [2, 0, 3]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    matrix = [
        [1, 0, 0, 0],
        [1, 1, 1, 1],
        [1, 0, 0, 0],
        [1, 0, 0, 0],
    ]
    assert solution(matrix, k=2) == [0, 2]


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    matrix = [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1],
    ]
    assert solution(matrix, k=3) == [1, 2, 3]


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    matrix = [
        [1, 0],
        [0, 0],
        [1, 0],
    ]
    assert solution(matrix, k=2) == [1, 0]

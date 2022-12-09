from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Scan
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_distance = float("inf")
        ans = -1
        for i, (pt_x, pt_y) in enumerate(points):
            if pt_x == x or pt_y == y:
                pt_distance = abs(x - pt_x) + abs(y - pt_y)
                if pt_distance < min_distance:
                    ans = i
                    min_distance = pt_distance
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "nearestValidPoint",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    points = [
        [1, 2],
        [3, 1],
        [2, 4],
        [2, 3],
        [4, 4],
    ]
    assert solution(3, 4, points) == 2


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    points = [
        [3, 4],
    ]
    assert solution(3, 4, points) == 0


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    points = [
        [2, 3],
    ]
    assert solution(3, 4, points) == -1

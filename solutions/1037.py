from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Math, Slope
    Time Complexity: O(1)
    Space Complexity: O(1)
    """

    def isBoomerang(self, points: List[List[int]]) -> bool:
        def slope(a, b):
            if a[0] == b[0]:
                return float("inf")
            else:
                return (b[1] - a[1]) / (b[0] - a[0])

        return (
            points[0] != points[1]
            and points[1] != points[2]
            and slope(points[0], points[1]) != slope(points[1], points[2])
        )


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "isBoomerang",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(points=[[1, 1], [2, 3], [3, 2]])


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert not solution(points=[[1, 1], [2, 2], [3, 3]])


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert not solution(points=[[0, 0], [1, 1], [1, 1]])

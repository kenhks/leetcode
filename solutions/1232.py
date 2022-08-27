from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Scan
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        dy, dx = (y1 - y0), (x1 - x0)
        return not any(dy * (x - x0) != dx * (y - y0) for x, y in coordinates)


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "checkStraightLine",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    coordinates = [
        [1, 2],
        [2, 3],
        [3, 4],
        [4, 5],
        [5, 6],
        [6, 7],
    ]
    assert solution(coordinates)


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    coordinates = [
        [1, 1],
        [2, 2],
        [3, 4],
        [4, 5],
        [5, 6],
        [7, 7],
    ]
    assert not solution(coordinates)


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    coordinates = [
        [0, 0],
        [0, 1],
        [0, -1],
    ]
    assert solution(coordinates)


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    coordinates = [
        [0, 0],
        [0, 1],
        [1, 0],
    ]
    assert not solution(coordinates)

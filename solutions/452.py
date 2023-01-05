from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Sort
    Time Complexity: O(nlog(2, n)) = nlog(2, n) + n
    Space Complexity: O(1)
    """

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        prev_end = points[0][-1]
        ans = 1
        for point in points[1:]:
            if point[0] > prev_end:
                ans += 1
                prev_end = point[1]
            else:
                prev_end = min(prev_end, point[1])
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "findMinArrowShots",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    points = [[10, 16], [2, 8], [1, 6], [7, 12]]
    assert solution(points) == 2


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    points = [[1, 2], [3, 4], [5, 6], [7, 8]]
    assert solution(points) == 4


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    points = [[1, 2], [2, 3], [3, 4], [4, 5]]
    assert solution(points) == 2

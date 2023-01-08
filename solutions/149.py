from typing import Dict, List, Tuple

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Hashmap
    Time Complexity: O(n^2)
    Space Complexity: O(n^2)
    """

    def maxPoints(self, points: List[List[int]]) -> int:
        max_count = 1
        point_slope_count: Dict[Tuple[float, int]] = {tuple(points[0]): {}}
        for x1, y1 in points[1:]:
            for x2, y2 in point_slope_count:
                if x1 == x2:
                    slope = float("inf")
                else:
                    slope = (y2 - y1) / (x2 - x1)
                point_slope_count[x2, y2][slope] = point_slope_count[x2, y2].get(slope, 1) + 1
                max_count = max(max_count, point_slope_count[x2, y2][slope])
            point_slope_count[x1, y1] = {}
        return max_count


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "maxPoints",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    points = [[1, 1], [2, 2], [3, 3]]
    assert solution(points) == 3


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
    assert solution(points) == 4

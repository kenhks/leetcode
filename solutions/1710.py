from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Sort by unit descending
    Time Complexity: O(nlog(2, n)) = nlog(2, n) + n
    Space Complexity: O(1)
    """

    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        ans = 0
        for box, unit in sorted(boxTypes, key=lambda x: x[1], reverse=True):
            used_box = min(box, truckSize)
            truckSize -= used_box
            ans += used_box * unit
            if truckSize == 0:
                break
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "maximumUnits",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    boxTypes = [[1, 3], [2, 2], [3, 1]]
    truckSize = 4
    assert solution(boxTypes, truckSize) == 8


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    boxTypes = [[5, 10], [2, 5], [4, 7], [3, 9]]
    truckSize = 10
    assert solution(boxTypes, truckSize) == 8

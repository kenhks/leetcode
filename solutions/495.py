from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Scan with pointer
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total = 0
        max_time = -1
        for i in timeSeries:
            if i > max_time:
                total += duration
                max_time = i + duration - 1
            else:
                new_max_time = i + duration - 1
                total += new_max_time - max_time
                max_time = new_max_time
        return total


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "findPoisonedDuration",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(timeSeries=[1, 4], duration=2) == 4


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(timeSeries=[1, 2], duration=2) == 3

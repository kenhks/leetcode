from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Convert time to integer
    Time Complexity: O(1)
    Space Complexity: O(1)
    """

    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        def time_to_number(str):
            return int(str[:2]) * 60 + int(str[-2:])

        x1, x2 = [time_to_number(i) for i in event1]
        y1, y2 = [time_to_number(i) for i in event2]
        return x1 <= y2 and y1 <= x2


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "haveConflict",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(event1=["01:15", "02:00"], event2=["02:00", "03:00"])


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(event1=["01:00", "02:00"], event2=["01:20", "03:00"])


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert not solution(event1=["10:00", "11:00"], event2=["14:00", "15:00"])

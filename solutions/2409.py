from typing import Tuple

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Math
    Time Complexity: O(1)
    Space Complexity: O(1)
    """

    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        calendar_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def str_to_days_in_year(date: str) -> Tuple[int, int]:
            return sum(calendar_days[: int(date[:2]) - 1]) + int(date[-2:])

        a_start = str_to_days_in_year(arriveAlice)
        a_end = str_to_days_in_year(leaveAlice)
        b_start = str_to_days_in_year(arriveBob)
        b_end = str_to_days_in_year(leaveBob)
        return max(min(b_end, a_end) - max(a_start, b_start) + 1, 0)


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "countDaysTogether",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(arriveAlice="08-15", leaveAlice="08-18", arriveBob="08-16", leaveBob="08-19") == 3


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(arriveAlice="10-01", leaveAlice="10-31", arriveBob="11-01", leaveBob="12-31") == 0


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(arriveAlice="10-20", leaveAlice="12-22", arriveBob="06-21", leaveBob="07-05") == 0

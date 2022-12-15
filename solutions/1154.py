import datetime

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Calendar Math
    Time Complexity: O(1)
    Space Complexity: O(1) = 12
    """

    def dayOfYear(self, date: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
        year = int(date[:4])
        month = int(date[5:7])
        ans = sum(days[: month - 1]) + int(date[-2:])
        if month >= 3 and (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
            ans += 1
        return ans


class Solution2:
    """
    Python built-in datetime
    Time Complexity: O(1)
    Space Complexity: O(1)
    """

    def dayOfYear(self, date: str) -> int:
        year, month, day = map(int, date.split("-"))
        return (datetime.date(year, month, day) - datetime.date(year, 1, 1)).days + 1


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "dayOfYear",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(date="2019-01-09") == 9


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(date="2019-02-10") == 41


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(date="2000-03-01") == 61


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert solution(date="2000-12-21") == 356


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert solution(date="2001-12-21") == 355

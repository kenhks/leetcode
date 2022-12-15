import datetime

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Math, modulo by 7 with offset
    Time Complexity: O(1)
    Space Complexity: O(1)
    """

    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        weekday_name = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        days_by_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
        offset_year, offset_weekday = 1971, 5

        def is_leap(year):
            return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

        for y in range(offset_year, year):
            offset_weekday += 1
            if is_leap(y):
                offset_weekday += 1
        days = sum(days_by_month[: month - 1]) + day - 1
        if month >= 3 and is_leap(year):
            days += 1
        return weekday_name[(days + offset_weekday) % 7]


class Solution2:
    """
    Python built-in datetime
    Time Complexity: O(1)
    Space Complexity: O(1)
    """

    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        return datetime.date(year, month, day).strftime("%A")


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "dayOfTheWeek",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(day=31, month=8, year=2019) == "Saturday"


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(day=18, month=7, year=1999) == "Sunday"


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(day=15, month=8, year=1993) == "Sunday"


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert solution(day=1, month=1, year=1971) == "Friday"


@pytest.mark.parametrize("solution", solutions)
def test_5(solution):
    assert solution(day=1, month=1, year=1972) == "Saturday"


@pytest.mark.parametrize("solution", solutions)
def test_6(solution):
    assert solution(day=1, month=1, year=1973) == "Monday"

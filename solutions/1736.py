import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Time Complexity: O(1)
    Space Complexity: O(1)
    """

    def maximumTime(self, time: str) -> str:
        hour, minute = time[:2], time[-2:]
        if hour == "??":
            hour = "23"
        elif hour[0] == "?":
            if ord(hour[1]) <= 51:
                hour = "2" + hour[1]
            else:
                hour = "1" + hour[1]
        elif hour[1] == "?":
            if hour[0] == "2":
                hour = "23"
            else:
                hour = hour[0] + "9"
        if minute == "??":
            minute = "59"
        elif minute[0] == "?":
            minute = "5" + minute[1]
        elif minute[1] == "?":
            minute = minute[0] + "9"
        return f"{hour}:{minute}"


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "maximumTime",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution("2?:?0") == "23:50"


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution("0?:3?") == "09:39"


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution("1?:22") == "19:22"

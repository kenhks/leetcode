import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Compare hour and min seperately
    Time Complexity: O(1)
    Space Complexity: O(1)
    """

    def convertTime(self, current: str, correct: str) -> int:
        ops_count = 0
        if current != correct:
            ops_count += int(correct[:2]) - int(current[:2])
            min_diff = int(correct[3:]) - int(current[3:])
            if min_diff < 0:
                ops_count -= 1
                min_diff += 60
            for step in [15, 5, 1]:
                if min_diff >= step:
                    step_count, min_diff = divmod(min_diff, step)
                    ops_count += step_count
        return ops_count


class Solution2:
    """
    calculate diff by minutes
    Time Complexity: O(1)
    Space Complexity: O(1)
    """

    def convertTime(self, current: str, correct: str) -> int:
        ops_count = 0
        min_diff = (
            int(correct[:2]) * 60
            + int(correct[3:])
            - int(current[:2]) * 60
            - int(current[3:])
        )
        for step in [60, 15, 5, 1]:
            if min_diff >= step:
                step_count, min_diff = divmod(min_diff, step)
                ops_count += step_count
        return ops_count


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "convertTime",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution("02:30", "04:35") == 3


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution("11:00", "11:01") == 1


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution("00:00", "00:00") == 0


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert solution("11:45", "12:00") == 1


@pytest.mark.parametrize("solution", solutions)
def test_5(solution):
    assert solution("11:45", "13:00") == 2

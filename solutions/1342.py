import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Time Complexity: O(log(2, n))
    Space Complexity: O(1)
    """

    def numberOfSteps(self, num: int) -> int:
        step = 0
        while num > 0:
            if num % 2 == 0:
                num = num >> 1
            else:
                num -= 1
            step += 1
        return step


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "numberOfSteps",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(14) == 6


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(8) == 4


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(123) == 12

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Time Complexity: O(1)
    Space Complexity: O(1)
    """

    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "sum",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(12, 5) == 17


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(-10, 4) == -6


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(0, 1) == 1

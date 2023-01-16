import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Math
    Time Complexity: O(1)
    Space Complexity: O(1)
    """

    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "divisorGame",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(n=2)


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert not solution(n=3)


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(n=1)

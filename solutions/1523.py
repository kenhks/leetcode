import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Math
    Time Complexity: O(1)
    Space Complexity: O(1)
    """

    def countOdds(self, low: int, high: int) -> int:
        offset = 0
        if low % 2 == 1:
            offset += 1
        elif high % 2 == 1:
            offset += 1
        return offset + (high - low) // 2


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "countOdds",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(3, 7) == 3


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(8, 10) == 1


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(8, 8) == 0


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert solution(1, 1) == 1


@pytest.mark.parametrize("solution", solutions)
def test_5(solution):
    assert solution(1, 10) == 5


@pytest.mark.parametrize("solution", solutions)
def test_6(solution):
    assert solution(10, 15) == 3

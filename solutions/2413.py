import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Math
    Time Complexity: O(1)
    Space Complexity: O(1)
    """

    def smallestEvenMultiple(self, n: int) -> int:
        return n if n % 2 == 0 else n * 2


class Solution2:
    """
    Math by bitwise operation
    Time Complexity: O(1)
    Space Complexity: O(1)
    """

    def smallestEvenMultiple(self, n: int) -> int:
        return n if n & 1 == 0 else n * 2


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "smallestEvenMultiple",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(5) == 10


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(6) == 6

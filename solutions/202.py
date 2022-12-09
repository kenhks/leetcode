import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Hashset
    Time Complexity: O(log(2, n))
    Space Complexity: O(log(2, n))
    """
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum([int(i) ** 2 for i in str(n)])
        return n == 1


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "isHappy",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(19)


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert not solution(2)


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert not solution(4)

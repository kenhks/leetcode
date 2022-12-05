import math

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Brute force with hashmap
    Time Complexity: O(c^(1/2))
    Space Complexity: O(n)
    """

    def judgeSquareSum(self, c: int) -> bool:
        ans = False
        c_sqrt = math.sqrt(c)
        if c_sqrt.is_integer() and c_sqrt ** 2 == c:
            ans = True
        else:
            seen = set()
            for i in range(0, math.ceil(c_sqrt)):
                i *= i
                if c - i in seen or 2 * i == c:
                    ans = True
                    break
                seen.add(i)
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "judgeSquareSum",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(5)


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert not solution(3)


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(121)


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert not solution(11)


@pytest.mark.parametrize("solution", solutions)
def test_5(solution):
    assert solution(2)

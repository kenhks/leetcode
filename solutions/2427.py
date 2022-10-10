import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Time Complexity: O(n) = log(2, min(a, b))
    Space Complexity: O(1)
    """

    def commonFactors(self, a: int, b: int) -> int:
        def gcd(a, b):
            if a < b:
                a, b = b, a
            while b > 0:
                a, b = b, a % b
            return a

        max_factor = gcd(a, b)
        if max_factor >= 2:
            ans = 2
            for i in range(2, gcd(a, b)):
                if a % i == 0 and b % i == 0:
                    ans += 1
        else:
            ans = 1
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "commonFactors",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(a=12, b=6) == 4


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(a=25, b=30) == 2


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(a=664, b=886) == 2


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert solution(a=43, b=945) == 1

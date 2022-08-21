import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Python built-in, convert number to binary string
    Time Complexity: O(log (nk(n-k)))
    Space Complexity: O(1)
    """
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")


class Solution2:
    """
    Bitwise manipulation
    Time Complexity: O(log(2, n))
    Space Complexity: O(1)
    """
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            n = n & (n - 1)
            ans += 1
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "hammingWeight",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(int("00000000000000000000000000001011", 2)) == 3


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(int("011", 2)) == 2


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(int("0000000000000000000001110001011", 2)) == 6

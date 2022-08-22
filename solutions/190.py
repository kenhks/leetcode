import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Python built-in, convert to string
    Time Complexity: O(log(2, n)) = 3log(2, n)
    Space Complexity: O(log(2, n)) = log(2, n)
    """

    def reverseBits(self, n: int) -> int:
        return int(f"{n:032b}"[::-1], 2)


class Solution2:
    """
    Bitwise operation
    Time Complexity: O(log(2, n))
    Space Complexity: O(1)
    """

    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            bit = (n >> i) & 1
            ans = ans | (bit << (31 - i))
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "reverseBits",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(int("00000010100101000001111010011100", 2)) == 964176192


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(int("11111111111111111111111111111101", 2)) == 3221225471

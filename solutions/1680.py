import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Concat binary string
    Time Complexity: O((n^2)log(2, n)) = Sum(1, n)(nlog(2, n))
    Space Complexity: O(log(n!)) =  Sum(1, n)(log(2, n))
    """

    def concatenatedBinary(self, n: int) -> int:
        s = ""
        for i in range(1, n + 1):
            s += f"{i:b}"
        return int(s, 2) % (10**9 + 7)


class Solution2:
    """
    Concat binary string
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def concatenatedBinary(self, n: int) -> int:
        modulo = 10**9 + 7
        shift, ans = 0, 0
        for i in range(1, n + 1):
            if i & (i - 1) == 0:  # i.bit_length()
                shift += 1
            ans = ((ans << shift) | i) % modulo
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "concatenatedBinary",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(1) == 1


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(3) == 27


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(12) == 505379714

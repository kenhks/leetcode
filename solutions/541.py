import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Time Complexity:
    Space Complexity:
    """

    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        for i in range(0, len(s), 2 * k):
            left = i
            right = min(i + k - 1, len(s) - 1)
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        return "".join(s)


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "reverseStr",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(s="abcdefg", k=2) == "bacdfeg"


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(s="abcd", k=2) == "bacd"

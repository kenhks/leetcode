import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Find ring distance
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def minTimeToType(self, word: str) -> int:
        ans = 0
        prev = "a"
        for c in word:
            diff = abs(ord(c) - ord(prev))
            ans += min(diff, 26 - diff) + 1
            prev = c
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "minTimeToType",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(word="abc") == 5


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(word="bza") == 7


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(word="zjpc") == 34

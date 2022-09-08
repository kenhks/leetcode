import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Use hashmap as counter
    Time Complexity: O(n) = n + 52
    Space Complexity: O(1) = 52
    """

    def longestPalindrome(self, s: str) -> int:
        counter = {}
        for c in s:
            if c in counter:
                counter[c] += 1
            else:
                counter[c] = 1
        size = extra = 0
        for c, count in counter.items():
            if count % 2 == 1:
                extra = 1
                count -= 1
            size += count
        return size + extra


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "longestPalindrome",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution("abccccdd") == 7


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution("a") == 1

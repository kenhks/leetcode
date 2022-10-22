from collections import Counter

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Check seen freq with hashmap
    Time Complexity: O(n)
    Space Complexity: O(1) = 26
    """

    def minDeletions(self, s: str) -> int:
        ans = 0
        seen = set()
        for k in Counter(s).values():
            while k in seen:
                k -= 1
                ans += 1
            if k > 0:
                seen.add(k)
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "minDeletions",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution("aab") == 0


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution("aaabbbcc") == 2


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution("ceabaacb") == 2

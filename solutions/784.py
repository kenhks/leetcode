from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Time Complexity: O(n*2^n)
    Space Complexity: O(n*2^n)
    n = len(s)
    """

    def letterCasePermutation(self, s: str) -> List[str]:
        ans = [""]
        for c in s:
            ans = [x + cc for x in ans for cc in {c, c.swapcase()}]
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "letterCasePermutation",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    expected = [
        "a1b2",
        "a1B2",
        "A1b2",
        "A1B2",
    ]
    assert sorted(solution("a1b2")) == sorted(expected)


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    expected = [
        "3z4",
        "3Z4",
    ]
    assert sorted(solution("3z4")) == sorted(expected)
